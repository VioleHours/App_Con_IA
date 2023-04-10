import openai
import config
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("💬[i red] ChatGPT en Python[/i red]")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "salir de la aplicación")
    table.add_row("new", "crear una nueva conversación")
    print(table)

        #Contexto del asistente 
    context = {"role": "system", 
                "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
             print("🆕 Nueva conversación creada")
             messages = [context]
             content = __prompt()

        #Contexto de las preguntas
        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                messages=messages)
        #Contexto de todas sus respuestas
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold red]> [/bold red] [red]{response_content}[/red]")

def __prompt() -> str:
    prompt = typer.prompt("¿Sobre qué quieres hablar?")

    if prompt == "exit":
        exit = typer.confirm("✋ ¿Estás seguro?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()
        
        return __prompt()
    
    return prompt


if __name__ == "__main__":
        typer.run(main)