import flet as ft
import actions
from components.app_bar import app_bar
from components.add_scale import scale_dialog
from components.scale_element import ScaleListItem
from components.search_bar import SearchBar

def create_scales_view(page: ft.Page):

    scales_listview = ft.ListView(
        expand=1,  
        spacing=8, 
        padding=ft.padding.all(20),
    )

    btn_add_element = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.BLUE_700,
        on_click=lambda e: scale_dialog(e.page, scales_listview)
    )
    
    search_bar = SearchBar(on_search=actions.handle_search_update)
    
    btn_export = ft.IconButton(
        icon=ft.Icons.PICTURE_AS_PDF_OUTLINED,
        icon_color=ft.Colors.BLUE_700,
        on_click=lambda e: print('Save clicado')
    )

    rw_add_and_search = ft.Row(
        controls=[
            btn_add_element,
            search_bar,
            btn_export
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    return ft.View(
        route='/scales',
        controls=[
            app_bar(),
            rw_add_and_search,
            ft.Divider(height=20,color=ft.Colors.TRANSPARENT),
            scales_listview
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        scroll = ft.ScrollMode.ADAPTIVE,   
    )

