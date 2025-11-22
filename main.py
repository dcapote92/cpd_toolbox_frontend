import flet as ft
from views.home_view import create_home_view
from views.login_view import create_login_view
from views.scales_view import create_scales_view 

def main(page: ft.Page):
    page.title = 'CPD ToolBox'

    def route_change(route):
        page.views.clear()

        page.views.append(create_login_view(page))

        if page.route == '/home':
            page.views.append(create_home_view(page))
        
        elif page.route == '/scales':
            page.views.append(create_home_view(page))
            page.views.append(create_scales_view(page))
            
        
        page.update()

    def view_pop(view: ft.View):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go('/')

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(target=main, assets_dir='assets')