from aiogram.fsm.state import StatesGroup, State


class BookingState(StatesGroup):
    day = State()
    time = State()
    event = State()
    is_repetitive = State()
