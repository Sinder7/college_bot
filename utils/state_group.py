from aiogram.fsm.state import StatesGroup, State

class GroupName(StatesGroup):
    user_group: str = State()

class GetNameGroupToday(StatesGroup):
    group_name = State()

class GetNameGroupTomorrow(StatesGroup):
    group_name = State()

class GetNameGroupWeek(StatesGroup):
    group_name = State()