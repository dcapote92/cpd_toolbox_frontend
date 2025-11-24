import flet as ft
from views.home_view import create_home_view
from views.login_view import create_login_view
from views.scales_view import create_scales_view 
from views.register_view import create_register_view

def main(page: ft.Page):
    page.title = 'CPD ToolBox'

    def route_change(route):
        page.views.clear()

        match(page.route):
            case '/' | '/login':
                page.views.append(create_login_view(page))

            case '/register':
                page.views.append(create_login_view(page))
                page.views.append(create_register_view(page))
            
            case '/home':
                page.views.append(create_home_view(page))

            case '/scales':
                page.views.append(create_home_view(page))
                page.views.append(create_scales_view(page))
            
            case _:
                page.views.append(create_login_view(page))
        
        page.update()

    def view_pop(view: ft.View):
        page.views.pop()
        
        if len(page.views) > 0:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go('/login')

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go('/login')

ft.app(target=main, assets_dir='assets')