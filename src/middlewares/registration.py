from wonda.bot import Blueprint, BaseMiddleware, Message
from src.database.user import User

bp = Blueprint("Registration middleware")


@bp.labeler.message_view.register_middleware
class RegistrationMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        user = await User.get_or_none(uid=self.update.from_.id)

        if user is None:
            await User.create(
                uid=self.update.from_.id, nickname=self.update.from_.username
            )

        self.send(
            {
                "user": user,
            }
        )
