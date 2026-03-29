import flet as ft

def main(page: ft.Page):
    # Setup page settings
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "My Lifestyle Tracker"
    
    # Create the content
    welcome_text = ft.Text("Welcome to your tracker!", size=30, weight="bold")
    setup_check = ft.Checkbox(label="I fixed the parenthesis error!", value=False)
    
    # Add content to the page
    page.add(welcome_text, setup_check)

# Run the app
if __name__ == "__main__":
    ft.app(target=main)