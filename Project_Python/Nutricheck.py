import gradio as gr # type: ignore

food_calories = {
    "egg": 78,
    "idly": 50,
    "bread": 80,
    "maaza":85,
    "cookies":40,
    "milk": 103,
    "banana": 105,
    "rice": 206,
    "apple": 95,
    "chicken": 239,
    "cheese": 113,
    "butter": 102,
    "orange": 62,
}


def Estimate_calories(Meal_input):
    items = Meal_input.lower().split(",")
    total_calories = 0
    result_lines = []

    for item in items:
        item = item.strip()
        for food in food_calories:
            if food in item:
                quantity = 1
                words = item.split()
                for word in words:
                    if word.isdigit():
                        quantity =int(word)

                calories = quantity * food_calories[food]
                total_calories += calories
                result_lines.append(f"{quantity} x {food} = {calories} cal")

    if not result_lines:
        return "Olunga Match aagura maari input kudunga..! try '2 eggs, 1 bread ' intha style la input kudunga..!"

    return f"total calories:  {total_calories} cal\n\n" + "\n".join(result_lines)

#Final step release in Gradio interface 

gr.Interface(
    fn=Estimate_calories,
    inputs=gr.Textbox(lines=3, placeholder="e.g.,2 eggs, 1 breadd"),
    outputs="text",
    title="<=== Dummy Baba Nutricheck ===>",
    description="Enter your Today's meal, And we will estimate the Calories====>!"
).launch()                