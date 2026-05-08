from app.schemas.evm_schema import EvmInput
from app.services.evm_calculation_service import EvmCalculationService


def test_calculate_pv() -> None:
    activity = EvmInput(bac=1000, planned_progress=25, actual_progress=0, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.pv == 250


def test_calculate_ev() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=40, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.ev == 400


def test_calculate_cv() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=300)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cv == 200


def test_calculate_sv() -> None:
    activity = EvmInput(bac=1000, planned_progress=60, actual_progress=40, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.sv == -200


def test_calculate_cpi_when_ac_gt_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=250)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi == 2


def test_calculate_cpi_none_when_ac_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=0)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.cpi is None


def test_calculate_spi_when_pv_gt_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=25, actual_progress=50, actual_cost=10)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.spi == 2


def test_calculate_spi_none_when_pv_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=0, actual_progress=50, actual_cost=10)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.spi is None


def test_project_summary_without_activities() -> None:
    summary = EvmCalculationService.calculate_project_summary([])
    assert summary.activity_count == 0
    assert summary.cpi is None
    assert summary.spi is None


def test_actual_progress_zero() -> None:
    activity = EvmInput(bac=1000, planned_progress=20, actual_progress=0, actual_cost=50)
    indicators = EvmCalculationService.calculate_activity_indicators(activity)
    assert indicators.ev == 0
    assert indicators.cv == -50
