import numpy as np
import pygame

#TODO: import the agent we end up making

class Controller:
    def __init__(self, mode='keyboard'):
        """
        Initializes controller object to unify input interface.

        Args:
            mode: str, determines mode of input control.
                Must be in ['keyboard', 'agent'].
        """
        self.mode = mode
        if mode == 'keyboard':
            pass
        elif mode == 'agent':
            pass
            # Initialize an agent
        else:
            raise NotImplementedError

    def process_input(self, map):
        """
        Process an input.

        Args:
            map: map object, used for agent.

        Returns:
            action: tuple, steer / acceleration action.
        """
        if self.mode == 'keyboard':
            action = self.process_keys()
        elif self.mode == 'agent':
            action = self.process_agent(env)
            # print("Action Taken", action)
        return action

    def process_keys(self):
        """
        Process an input from the keyboard.

        Returns:
            action: tuple, steer / acceleration action.
        """
        action_dict = {'steer': 0.0, 'acc': 0.0}
        steer, acc = 1, 1
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            acc = 2
        elif keys[pygame.K_DOWN]:
            acc = 0
        if keys[pygame.K_LEFT]:
            steer = 0
        elif keys[pygame.K_RIGHT]:
            steer = 2
        action = (acc, steer)
        return action

    def process_agent(self, map):
        """
        Process an input from the agent.

        Args: 
            map: map object, used for agent.
        Returns:
            action: tuple, steer / acceleration action.
        """
        steer = self.agent.eval_policy(map, None)
        acc = 0 # TODO: FIX
        action = (steer, acc)
        return action

    def reset(self):
        """
        Resets the controller, used for agent.
        """
        if self.mode == 'keyboard':
            pass
        elif self.mode == 'xbox':
            pass
        elif self.mode == 'agent':
            self.agent.reset()