import flet as ft

def create_login_view(page: ft.Page):
    
    edt_user = None
    edt_password = None

    def validate_fields():
        is_valid = True

        if not edt_user:
            edt_user.error_text = 'Usuário é obrigatório.'
            is_valid = False
        else: edt_user.error_text=None # get error message cleaned if the field is valid

        if not edt_password or len(edt_password) < 8:
            edt_password.error_text = 'A senha deve ter entre 8 e 15 caracteres.'
            is_valid = False
        else: edt_password.error_text=None

        edt_user.update()
        edt_password.update()

        return is_valid
        

    def login(e):
        page.go('/home')
        ''' if validate_fields():
            page.snack_bar = ft.SnackBar(
                ft.Text(f'Login bem-sucedido!'),
                bgcolor=ft.Colors.GREEN_700)
            page.go('/home')
            page.open(page.snack_bar)
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text(f'Por favor corrija os erros nos campos antes de continuar.!'),
                bgcolor=ft.Colors.RED_700,
                duration=3000
            )
            page.open(page.snack_bar)
            page.update()'''

    def register(e):
        page.go('/register')


    img_logo = ft.Image(
        src='logo.png',
        width=200,
        height=200,
        fit=ft.ImageFit.FILL
    )

    img_container = ft.Container(
        content=img_logo,
        alignment=ft.alignment.top_center,
        padding=ft.padding.only(top=10, bottom=30)
    )

    edt_user = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=36,
        label='Usuário',
        enable_suggestions=True,
        autofocus=True,
        capitalization= ft.TextCapitalization.CHARACTERS
    )
    
    edt_password = ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        multiline=False,
        max_length=15,
        label='Senha',
        password=True,
        can_reveal_password=True
    )

    btn_login = ft.ElevatedButton(
        text='Entrar',
        icon= ft.Icons.LOGIN,
        width=120,
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
        on_click=login
    )

    btn_register = ft.ElevatedButton(
        text='Registrar',
        icon= ft.Icons.PERSON_ADD_ALT_1,
        width=120,
        bgcolor=ft.Colors.GREEN_700,
        color=ft.Colors.WHITE,
        on_click=register
    )

    rw_buttons = ft.Row(
        controls=[
            btn_login,
            btn_register
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

    box_container = ft.Container(
        height=600,
        width=400,
        border=ft.border.all(width=3, color=ft.Colors.BLUE_GREY_500),
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                img_container,
                edt_user,
                edt_password,
                ft.Divider(height=20,color=ft.Colors.TRANSPARENT),
                rw_buttons
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=30,
    )



    return ft.View(
        route='/login',
        controls=[
            box_container,
            ft.Text('©2025 Daniel Capote')
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
