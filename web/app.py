from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView

from db import db
from db.models import Category, Product

from web.provider import UsernameAndPasswordProvider

app = Starlette()
admin = Admin(db._engine,
              title="Movie Bot",
              base_url= "/",
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="sdgfhjhhsfdghn")]
              )

admin.add_view(ModelView(Category))
admin.add_view(ModelView(Product))

admin.mount_to(app)