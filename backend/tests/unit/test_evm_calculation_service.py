import pytest
from pydantic import ValidationError

from app.schemas.evm_schema import EvmInput
from app.services.evm_calculation_service import EvmCalculationService


def test_calculate_pv_correctly() -> None:
    activity = EvmInput(bac=1000, planned_progress=25, actual_progress=0, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.pv == 250


def test_calculate_ev_correctly() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=40, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.ev == 400


def test_calculate_cv_correctly() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=300)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cv == 200


def test_calculate_sv_correctly() -> None:
    activity = EvmInput(bac=1000, planned_progress=60, actual_progress=40, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.sv == -200


def test_calculate_cpi_when_actual_cost_is_greater_than_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=250)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi == 2


def test_return_cpi_none_when_actual_cost_is_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=10, actual_progress=50, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi is None


def test_calculate_spi_when_pv_is_greater_than_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=25, actual_progress=50, actual_cost=10)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.spi == 2


def test_return_spi_none_when_pv_is_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=10)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.spi is None


def test_return_eac_when_cpi_is_valid() -> None:
    activity = EvmInput(bac=1000, planned_progress=50, actual_progress=50, actual_cost=250)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi == 2
    assert indicators.eac == 500


def test_return_eac_none_when_cpi_is_none() -> None:
    activity = EvmInput(bac=1000, planned_progress=50, actual_progress=50, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi is None
    assert indicators.eac is None


def test_return_vac_when_eac_is_valid() -> None:
    activity = EvmInput(bac=1000, planned_progress=50, actual_progress=50, actual_cost=250)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.vac == 500


def test_return_vac_none_when_eac_is_none() -> None:
    activity = EvmInput(bac=1000, planned_progress=50, actual_progress=50, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.eac is None
    assert indicators.vac is None


def test_handle_actual_progress_equals_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=20, actual_progress=0, actual_cost=50)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.ev == 0
    assert indicators.cpi == 0
    assert indicators.eac is None
    assert indicators.vac is None


def test_handle_project_without_activities() -> None:
    summary = EvmCalculationService.calculate_project_summary([])
    assert summary.activity_count == 0
    assert summary.total_bac == 0
    assert summary.total_pv == 0
    assert summary.total_ev == 0
    assert summary.total_ac == 0
    assert summary.cpi is None
    assert summary.spi is None
    assert summary.total_eac is None
    assert summary.total_vac is None


def test_calculate_consolidated_project_summary_correctly() -> None:
    activities = [
        EvmInput(bac=1000, planned_progress=50, actual_progress=40, actual_cost=300),
        EvmInput(bac=2000, planned_progress=25, actual_progress=50, actual_cost=700),
    ]
    summary = EvmCalculationService.calculate_project_summary(activities)

    assert summary.activity_count == 2
    assert summary.total_bac == 3000
    assert summary.total_pv == 1000
    assert summary.total_ev == 1400
    assert summary.total_ac == 1000
    assert summary.total_cv == 400
    assert summary.total_sv == 400
    assert summary.cpi == pytest.approx(1.4)
    assert summary.spi == pytest.approx(1.4)
    assert summary.total_eac == pytest.approx(2142.857142857143)
    assert summary.total_vac == pytest.approx(857.1428571428571)


def test_consolidated_cpi_and_spi_are_calculated_from_totals_not_averages() -> None:
    activities = [
        EvmInput(bac=100, planned_progress=50, actual_progress=50, actual_cost=25),
        EvmInput(bac=100, planned_progress=100, actual_progress=50, actual_cost=100),
    ]

    summary = EvmCalculationService.calculate_project_summary(activities)

    activity_one = EvmCalculationService.calculate_activity_indicators(activities[0])
    activity_two = EvmCalculationService.calculate_activity_indicators(activities[1])
    assert activity_one.cpi is not None and activity_two.cpi is not None
    assert activity_one.spi is not None and activity_two.spi is not None
    average_cpi = (activity_one.cpi + activity_two.cpi) / 2
    average_spi = (activity_one.spi + activity_two.spi) / 2

    assert summary.cpi == pytest.approx(0.8)
    assert summary.spi == pytest.approx(2 / 3)
    assert summary.cpi != pytest.approx(average_cpi)
    assert summary.spi != pytest.approx(average_spi)


def test_interpret_cpi_greater_than_one() -> None:
    assert EvmCalculationService.interpret_cpi(1.2) == "Eficiente en costos"


def test_interpret_cpi_equal_to_one() -> None:
    assert EvmCalculationService.interpret_cpi(1.0) == "En presupuesto"


def test_interpret_cpi_less_than_one() -> None:
    assert EvmCalculationService.interpret_cpi(0.8) == "Sobre presupuesto"


def test_interpret_spi_greater_than_one() -> None:
    assert EvmCalculationService.interpret_spi(1.2) == "Adelantado"


def test_interpret_spi_equal_to_one() -> None:
    assert EvmCalculationService.interpret_spi(1.0) == "En cronograma"


def test_interpret_spi_less_than_one() -> None:
    assert EvmCalculationService.interpret_spi(0.8) == "Atrasado"


def test_handle_bac_equals_zero() -> None:
    activity = EvmInput(bac=0, planned_progress=80, actual_progress=20, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.pv == 0
    assert indicators.ev == 0
    assert indicators.cv == 0
    assert indicators.sv == 0
    assert indicators.cpi is None
    assert indicators.spi is None
    assert indicators.eac is None
    assert indicators.vac is None


def test_invalid_percentages_raise_validation_error() -> None:
    with pytest.raises(ValidationError):
        EvmInput(bac=1000, planned_progress=-1, actual_progress=10, actual_cost=100)

    with pytest.raises(ValidationError):
        EvmInput(bac=1000, planned_progress=10, actual_progress=101, actual_cost=100)
