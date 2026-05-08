from app.schemas.evm_schema import (
    ActivityEvmIndicators,
    EvmInput,
    EvmStatus,
    ProjectEvmSummary,
)


class EvmCalculationService:
    @staticmethod
    def calculate_activity_indicators(activity_input: EvmInput) -> ActivityEvmIndicators:
        pv = (activity_input.planned_progress / 100) * activity_input.bac
        ev = (activity_input.actual_progress / 100) * activity_input.bac
        cv = ev - activity_input.actual_cost
        sv = ev - pv

        cpi = None if activity_input.actual_cost == 0 else ev / activity_input.actual_cost
        spi = None if pv == 0 else ev / pv

        eac = None if cpi in (None, 0) else activity_input.bac / cpi
        vac = None if eac is None else activity_input.bac - eac

        cpi_status = EvmCalculationService.interpret_cpi(cpi)
        spi_status = EvmCalculationService.interpret_spi(spi)
        status = EvmStatus(cpi_status=cpi_status, spi_status=spi_status)

        return ActivityEvmIndicators(
            pv=pv,
            ev=ev,
            cv=cv,
            sv=sv,
            cpi=cpi,
            spi=spi,
            eac=eac,
            vac=vac,
            cpi_status=cpi_status,
            spi_status=spi_status,
            status=status,
        )

    @staticmethod
    def calculate_project_summary(activities: list[EvmInput]) -> ProjectEvmSummary:
        if not activities:
            cpi_status = EvmCalculationService.interpret_cpi(None)
            spi_status = EvmCalculationService.interpret_spi(None)
            return ProjectEvmSummary(
                activity_count=0,
                total_bac=0.0,
                total_pv=0.0,
                total_ev=0.0,
                total_ac=0.0,
                total_cv=0.0,
                total_sv=0.0,
                total_eac=None,
                total_vac=None,
                cpi=None,
                spi=None,
                cpi_status=cpi_status,
                spi_status=spi_status,
                status=EvmStatus(cpi_status=cpi_status, spi_status=spi_status),
            )

        total_bac = sum(activity.bac for activity in activities)
        total_pv = sum((activity.planned_progress / 100) * activity.bac for activity in activities)
        total_ev = sum((activity.actual_progress / 100) * activity.bac for activity in activities)
        total_ac = sum(activity.actual_cost for activity in activities)
        total_cv = total_ev - total_ac
        total_sv = total_ev - total_pv

        cpi = None if total_ac == 0 else total_ev / total_ac
        spi = None if total_pv == 0 else total_ev / total_pv

        total_eac = None if cpi in (None, 0) else total_bac / cpi
        total_vac = None if total_eac is None else total_bac - total_eac

        cpi_status = EvmCalculationService.interpret_cpi(cpi)
        spi_status = EvmCalculationService.interpret_spi(spi)

        return ProjectEvmSummary(
            activity_count=len(activities),
            total_bac=total_bac,
            total_pv=total_pv,
            total_ev=total_ev,
            total_ac=total_ac,
            total_cv=total_cv,
            total_sv=total_sv,
            total_eac=total_eac,
            total_vac=total_vac,
            cpi=cpi,
            spi=spi,
            cpi_status=cpi_status,
            spi_status=spi_status,
            status=EvmStatus(cpi_status=cpi_status, spi_status=spi_status),
        )

    @staticmethod
    def interpret_cpi(cpi: float | None) -> str:
        if cpi is None:
            return "No calculable"
        if cpi > 1:
            return "Eficiente en costos"
        if cpi == 1:
            return "En presupuesto"
        return "Sobre presupuesto"

    @staticmethod
    def interpret_spi(spi: float | None) -> str:
        if spi is None:
            return "No calculable"
        if spi > 1:
            return "Adelantado"
        if spi == 1:
            return "En cronograma"
        return "Atrasado"
