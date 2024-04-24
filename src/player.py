import string
import time
from globals import *
from airtest.core.api import *

def set_device(func):
    """
    A decorator that sets the current device before calling the decorated function.

    Args:
        func (callable): The function to be decorated. This function should be a method of a class that has a 'dev' attribute.

    Returns:
        callable: The decorated function, which will call 'set_current(self.dev)' before calling the original function.
    """
    def wrapper(self, *args, **kwargs):
        set_current(self.serialNo)
        return func(self, *args, **kwargs)
    return wrapper

class Account:
    
    def __init__(self, device_url: string):
        self.dev = connect_device(device_url)
        self.serialNo = device_url.split('/')[-1]
        
    def __touch_until_appears(self, pos, result_template: Template, timeout: int = None) -> tuple:
        """
        Touches a specific position and waits until another result_template appears.
        If result_template does not appear within the timeout, pos is touched again.

        Args:
            pos (Template, coordinate(x,y)): The position to be touched.
            result_template (Template): The template to wait for.
            timeout (int): The maximum time to wait for result_template (in seconds).

        Returns:
            tuple: Returns the coordinate of the appeared template if result_template appears within the timeout, False otherwise.
        """
        start_time = time.time()
        while True:
            if isinstance(pos, Template) and exists(pos):
                touch(pos, duration=0.2)
            elif isinstance(pos, tuple):
                touch(pos, duration=0.2)
            exists_result = exists(result_template)
            if exists_result:
                return exists_result
            if timeout is not None and time.time() - start_time > timeout:
                raise TimeoutError("Operation timed out")

    def __touch_until_disappear(self, template: Template, pos = None, timeout: int = None):
        """Define a function to continuously click a specific template until it disappears

        Args:
            template (Template): The template to be checked and should be disappeared.
            pos (Template, coordinate(x,y)): The position to be touched. If None, the template is touched.
            timeout (int): The maximum time to wait for result_template (in seconds).

        Returns:
            bool: Returns True if the template disappears, False otherwise.
        """
        start_time = time.time()
        result_exists = exists(template)
        while result_exists:
            if pos is not None:
                touch(pos, duration=0.2)
            else:
                touch(result_exists, duration=0.2)
            sleep(1)
            result_exists = exists(template)
            if result_exists == False:
                return True
            if timeout is not None and time.time() - start_time > timeout:
                raise TimeoutError("Operation timed out")
        return False
    
    def __check_player_amount(self, player_amount: int):
        """Check if multi player or not
        
        Args:
            player_amount (int): The amount of players in the game
        """
        if player_amount > 1:
            self.__touch_until_appears(multi_player, with_friends)
            self.__touch_until_appears(with_friends, Attack)
            # TODO: add reward box choose
            self.__touch_until_appears(Attack, Waiting)
        else:
            self.__touch_until_appears(single_player, replace_helper)
            self.__touch_until_appears((200,380), Attack)
            # TODO: add reward box choose
            return

    @set_device
    def choose_map(self, map_name: string, player_amount: int):
        """Chooses a map based on the provided map name.

        Args:
            map_name (string): The name of the map to be chosen.
            player_amount (int): The amount of players in the game
        """
        # Set a timeout (in seconds)
        timeout = 60  # Change this to your desired timeout
        start_time = time.time()
    
        # First click initial to make sure the initial page is displayed
        if not exists(Join):
            self.__touch_until_appears(Initial, Join)
        # Check the map to be entered
        if map_name == 'Training':
            # Click the map entrance
            self.__touch_until_appears((200,550), Adventure)
            # Go to the grow map
            self.__touch_until_appears(Grow, Training)
            # Go into the training stage
            self.__touch_until_appears(Training, Back)
            # Deal with different training stages
            while True: #loop to search for dedicated stages
                if time.time() - start_time > timeout:
                    print("Timeout!")
                    return False
                if exists(Exp_exist): # exp stage
                    # Go to the prepare screen
                    self.__touch_until_appears(Exp_exist, Exp_stage)
                    self.__touch_until_appears(Exp_stage, multi_player)
                    self.__check_player_amount(1)
                    break
                elif exists(start_point): # start point stage is new
                    self.__touch_until_appears(start_point, Consume)
                    finished = find_all(Finished)
                    if finished is None: # no stages finished
                        self.__touch_until_appears((180,560), multi_player)
                    elif len(finished) == 1:
                        self.__touch_until_appears((180,480), multi_player)
                    elif len(finished) == 2:
                        self.__touch_until_appears((180,400), multi_player)
                    self.__check_player_amount(1)
                    break
                elif exists(new_stage): # new stage
                    self.__touch_until_appears(new_stage, Consume)
                    self.__touch_until_appears((180,400), multi_player)
                    self.__check_player_amount(1)
                    break
                # TODO: add final stage check
                else: # no stages meet the requirements # TODO: need refactor, support multi and single
                    swipe((180,300),(180,520),duration=0.2)
                    sleep(1)
                    continue
        elif map_name == 'Repeat':
            # Go to repeat map
            if player_amount > 1:
                self.__touch_until_appears(short_cut, Attack, timeout)
                # TODO: add reward box choose
                self.__touch_until_appears(Attack, Waiting, timeout)
            # TODO: add self-mode for repeat
        elif map_name == 'Temple':
            # Go to the temple map
            # Click the map entrance
            self.__touch_until_appears((200,550), Adventure)
            # Go to the grow map
            self.__touch_until_appears(Grow, Temple)
            # Go into the temple stage
            self.__touch_until_appears(Temple, Back)
            # Swipe to choose dark temple
            swipe((200,500),(200,300),duration=0.2)
            while not exists(dark_temple): # Check if dark temple exist
                swipe((200,500),(200,300),duration=0.2)
            self.__touch_until_appears(dark_temple, time_temple_second)
            self.__touch_until_appears(time_temple_second, multi_player)
            self.__check_player_amount(player_amount)
        return True
    
    @set_device
    def join(self, failed_times: int = 5):
        """Join the stage
        """
        # First click initial to make sure the initial page is displayed
        if not exists(Join):
            self.__touch_until_appears(Initial, Join)
        self.__touch_until_disappear(Join)
        # check if join successfully
        while True:
            sleep(2) # Add sleep to reduce judge time
            if exists(room_exist): # search successfully
                self.__touch_until_disappear(re_search, pos=(200,240))
                self.__touch_until_disappear(Attack)
                break
            elif exists(not_search): # Not search a room
                failed_times -= 1
                if failed_times == 0:
                    raise TimeoutError("Failed to join the stage")
                self.__touch_until_appears(re_search, Searching)
            elif exists(position_get): # Position get window comes
                self.__touch_until_disappear(passOk)
            elif exists(Searching): # searching
                continue

    @set_device
    def start_stage(self, player_amount: int):
        """Start the stage
        """
        if player_amount > 1:
            # waiting for other players to join
            while True:
                slot = find_all(Waiting)
                if slot is None and player_amount == 4:
                    self.__touch_until_disappear(change_order, pos = (200,600))
                    break
                elif slot is not None and (4 - len(slot)) == player_amount:
                    self.__touch_until_appears((200,600), final_check)
                    self.__touch_until_disappear(Yes)
                    break
                sleep(1)
        else:
            self.__touch_until_disappear(Attack)

    @set_device
    def pass_level(self):
        """Pass the level and get the reward, then back to the initial page
        """
        count = 0
        # pass the stage
        while True:
            count += 1
            swipe((200,350),(100,300),duration=1)
            sleep(1)
            if exists(passOk):
                if exists(stage_over):
                    self.__touch_until_disappear(passOk)
                    break
                else:
                    self.__touch_until_disappear(passOk)
            if count == 10:
                count = 0 # reset count
                if exists(Resurrection):
                    self.__touch_until_disappear(Yes)
        # pass the reward
        while True:
            touch((200,350), duration=0.2)
            sleep(1)
            # TODO:check luck max
            # luck max ok position (200,420)
            if self.__touch_until_disappear(resultOk):
                break
        # Check if choose fruit
        try:
            wait(choose_fruit, timeout=3)
            # Choose Fruit
            while True:
                if exists(choose_fruit_done):
                    self.__touch_until_disappear(passOk)
                    break
                sleep(0.5)
            # TODO: add automatic choose fruit
        except:
            pass
        # back to the initial page
        result_exists = exists(Initial)
        while not result_exists:
            touch((200,350), duration=0.2)
            sleep(1)
            result_exists = exists(Initial)
        # Check 3 times if need to close some windows
        for _ in range(2):
            if exists(Close):
                self.__touch_until_disappear(Close)
                break
            sleep(0.5)
