from fast_xabhelper.helpful import add_route, add_model
from fast_xabhelper.mount_logic import BaseMount


class Mount(BaseMount):
    """
    Монтирование зависимостей
    """

    def mount_route(self):
        import fast_xabhelper.admin_pack.fast_admin
        import fast_xabhelper.session_pack.fast_session
        import fast_xabhelper.user_pack.fast_user
        add_route(self.app, fast_xabhelper.user_pack.fast_user.router,
                  name="user_pack")
        add_route(self.app, fast_xabhelper.session_pack.fast_session.router,
                  name="session_pack")
        add_route(self.app, fast_xabhelper.admin_pack.fast_admin.router,
                  path_static="/home/denis/PycharmProjects/fastApiProject/fast_xabhelper/admin_pack/static/",
                  absolute=True,
                  name="admin_pack")

    def mount_model(self):
        from fast_xabhelper.user_pack.model import User
        from photo.model import Photo
        add_model(Photo)
        add_model(User)

    def mount_admin_panel(self):
        from fast_xabhelper.admin_pack.admin_base import Admin
        from fast_xabhelper.user_pack.admin import UserPanel

        Admin.add_panel(UserPanel())