from app.schemas.evm_schema import ActivityIndicators, EvmInput, ProjectSummary


class EvmCalculationService:
    @staticmethod
    def calculate_activity_indicators(activity: EvmInput) -> ActivityIndicators:
        pv = (activity.planned_progress / 100) * activity.bac
        ev = (activity.actual_progress / 100) * activity.bac
        cv = ev - activity.actual_cost
        sv = ev - pv

        cpi = None if activity.actual_cost == 0 else ev / activity.actual_cost
        spi = None if pv == 0 else ev / pv

        eac = None
        vac = None
        if cpi not in (None, 0):
            eac = activity.bac / cpi
            vac = activity.bac - eac

        return ActivityIndicators(
            pv=pv,
            ev=ev,
            cv=cv,
            sv=sv,
            cpi=cpi,
            spi=spi,
            eac=eac,
            vac=vac,
            cpi_status=EvmCalculationService.interpret_cpi(cpi),
            spi_status=EvmCalculationService.interpret_spi(spi),
        )

    @staticmethod
    def calculate_project_summary(activities: list[EvmInput]) -> ProjectSummary:
        if not activities:
            return ProjectSummary(
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
                cpi_status=EvmCalculationService.interpret_cpi(None),
                spi_status=EvmCalculationService.interpret_spi(None),
            )

        activity_indicators = [
            EvmCalculationService.calculate_activity_indicators(activity)
            for activity in activities
        ]

        total_bac = sum(activity.bac for activity in activities)
        total_pv = sum(indicator.pv for indicator in activity_indicators)
        total_ev = sum(indicator.ev for indicator in activity_indicators)
        total_ac = sum(activity.actual_cost for activity in activities)
        total_cv = total_ev - total_ac
        total_sv = total_ev - total_pv

        cpi = None if total_ac == 0 else total_ev / total_ac
        spi = None if total_pv == 0 else total_ev / total_pv

        total_eac = None
        total_vac = None
        if cpi not in (None, 0):
            total_eac = total_bac / cpi
            total_vac = total_bac - total_eac

        return ProjectSummary(
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
            cpi_status=EvmCalculationService.interpret_cpi(cpi),
            spi_status=EvmCalculationService.interpret_spi(spi),
        )

    @staticmethod
    def interpret_cpi(cpi: float | None) -> str:
        if cpi is None:
            return "CPI no calculable cuando AC = 0"
        if cpi > 1:
            return "eficiencia en costos"
        if cpi == 1:
            return "en presupuesto"
        return "sobre presupuesto"

    @staticmethod
    def interpret_spi(spi: float | None) -> str:
        if spi is None:
            return "SPI no calculable cuando PV = 0"
        if spi > 1:
            return "adelantado"
        if spi == 1:
            return "en cronograma"
        return "atrasado"
