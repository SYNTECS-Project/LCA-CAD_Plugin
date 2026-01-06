from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class LifeCyclePhase(Enum):
    """Enumeration of life-cycle phases in LCA"""
    OVERALL = "C"
    PRODUCTION = "D"
    SURFACE_TREATMENT = "E"
    USE_AND_MAINTENANCE = "F"
    END_OF_LIFE = "G"
    
    def __str__(self):
        return f'{self.name}'
    
class FactorType(Enum):
    """Enumeration of impact factor types"""
    GLOBAL_WARMING = 3
    OZONE_DEPLETION = 4
    IONIZING_RADIATION = 5
    PHOTOCHEMICAL_OZONE_FORMATION = 6 # e 8 
    FINE_PARTICULATE_MATTER_FORMATION = 7
    ACIDIFICATION = 9
    EUTROPHICATION = 10 # e 11
    ECOTOXICITY = 12 # e 13,14,15,16
    LAND_USE = 17
    RESOURCE_DEPLETION_MINERAL = 18 
    RESOURCE_DEPLETION_FOSSIL = 19
    WATER_CONSUMPTION = 20
    
    def getValues(self):
        if self is FactorType.PHOTOCHEMICAL_OZONE_FORMATION:    
            return [self.value, 8]
        elif self is FactorType.EUTROPHICATION:
            return [self.value, 11] 
        elif self is FactorType.ECOTOXICITY:
            return [self.value, 13, 14, 15, 16]
        else:
             return [self.value]
        
    def __str__(self):
        return f'{self.name}'


@dataclass
class Factor:
    """Represents an environmental impact factor"""
    name: str
    unit: str
    cell: int

@dataclass
class Phase:
    name: str
    cell: int

'''@dataclass
class LifeCyclePhaseImpact:
    """Represents impact data for a specific life-cycle phase"""
    phase: LifeCyclePhase
    impact_factors: Dict[str, ImpactFactor]
    
    def add_impact_factor(self, factor: ImpactFactor) -> None:
        self.impact_factors[factor.name] = factor

@dataclass
class ProductLCA:
    """Main data structure for product life-cycle assessment"""
    product_name: str
    phases: List[LifeCyclePhaseImpact]
    
    def get_phase_impacts(self, phase: LifeCyclePhase) -> Dict[str, ImpactFactor]:
        for phase_impact in self.phases:
            if phase_impact.phase == phase:
                return phase_impact.impact_factors
        return {}
'''