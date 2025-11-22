import flet as ft
import actions
from components.app_bar import app_bar
from components.search_bar import SearchBar

def create_scales_view(page: ft.Page):
    

    scales_listview = ft.ListView(
        expand=1,  
        spacing=8, 
        padding=ft.padding.all(20),
        controls=[]
    )
     
    edt_num = ft.TextField(
        multiline=False,
        max_length=3,
        autofocus=True,
        enable_suggestions=True,
        hint_text='000',
        border=ft.OutlinedBorder(),
        keyboard_type=ft.KeyboardType.NUMBER,
        width=120,
        label='Número',
        data='num'
    )
    
    edt_model = ft.TextField(
        multiline=False,
        max_length=15,
        autofocus=True,
        enable_suggestions=True,
        hint_text='prix5-plus',
        border=ft.OutlinedBorder(),
        keyboard_type=ft.KeyboardType.NAME,
        width=120,
        label='Modelo',
        data='model'
    )
    
    dropd_section = ft.Dropdown(
        label='Setor',
        hint_text='Selecione...',
        width=160,
        options=[
            ft.dropdown.Option(section) for section in ['Açougue', 'Frios', 'Padaria']
        ]
    )
    
    edt_weight = ft.TextField(
        multiline=False,
        max_length=30,
        autofocus=True,
        enable_suggestions=True,
        hint_text='20.000',
        border=ft.OutlinedBorder(),
        keyboard_type=ft.KeyboardType.NUMBER,
        width=120,
        label='Peso'
    )

    add_scale_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text('Adicionar Balança'),
        actions_alignment=ft.MainAxisAlignment.END,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            width=200,
            height=200,
            controls=[ edt_num, edt_model, dropd_section, edt_weight]
        )
    )


    def open_add_dialog(e):
        page.dialog = add_scale_dialog
        page.open(add_scale_dialog)
        page.update()

    def close_dialog(e):
        page.close(add_scale_dialog)
        edt_num.value = ""
        edt_model.value = ""
        dropd_section.value = None
        edt_weight.value = ""
        page.snack_bar = ft.SnackBar(
            ft.Text('Ação Cancelada!')
        )
        page.open(page.snack_bar)
        page.update()

    add_scale_dialog.actions=[
        ft.TextButton('Ok', on_click=lambda e:actions.add_listview_element(
            edt_num,
            edt_model,
            dropd_section,
            edt_weight,
            scales_listview,
            page,
            add_scale_dialog
            ),
        data='Ok'),
        ft.TextButton('Cancelar', on_click=close_dialog, data='Cancelar'),
    ]

    btn_add_element = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=lambda e: open_add_dialog(e)
    )
    
    search_bar = SearchBar(on_search=actions.handle_search_update)

    
    btn_export = ft.IconButton(
        icon=ft.Icons.PICTURE_AS_PDF_OUTLINED,
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
        scales_listview
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        scroll = ft.ScrollMode.ADAPTIVE,   
    )

