from une_ai.models import Agent
from une_ai.models import GridMap

class ConnectFourPlayer(Agent):

    def __init__(self, agent_name, agent_program):
        super().__init__(agent_name, agent_program)

    # TODO
    # add all the necessary sensors as per the requirements
    def add_all_sensors(self):
        self.add_sensor("game-board-sensor", GridMap(7, 6, None), lambda grid : isinstance(grid, GridMap))
        self.add_sensor('powerups-sensor', {'R':None , 'Y':None}, lambda val: isinstance(val, dict))
        self.add_sensor('turn-taking-indicator', 'Y', lambda v : isinstance(v, str))
    
    # TODO
    # add all the necessary actuators as per the requirements
    def add_all_actuators(self):
        self.add_actuator('checker-handler',  ('release', 0), lambda v: isinstance(v, tuple))
        self.add_actuator('powerup-selector', False, lambda v: isinstance(v, bool) )
    
    # TODO
    # add all the necessary actions as per the requirements
    def add_all_actions(self):
        for column in range(7):
            self.add_action(f'release-{column}',  lambda col=column: {'checker-handler':('release', col)})
            self.add_action(f'popup-{column}', lambda col=column: {'checker-handler':('popup', col)})
            self.add_action(f'use-power-up-{column}', lambda :{"powerup-selector" : True})