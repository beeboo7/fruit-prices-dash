from dash import Dash, Input, Output, html , dcc

app = Dash(__name__)

data = {
    "Fruits": ["Apples", "Oranges", "Bananas", "Grapes", "Pineapples"],
    "Prices": [1.2, 0.8, 0.5, 2.0, 3.5]
}



app.layout = html.Div([
    html.Div([
        html.H1("Fruit Prices"),
    ]),
    html.Div([
        dcc.Graph(
            id='bar-chart',
            figure={}
        )
    ]),
    html.Div([
        dcc.Dropdown(
            id='fruit-dropdown',
            multi=True,
            options=[{'label': fruit, 'value': fruit} for fruit in data['Fruits']],
            value=['Apples']
        ),
    ])
])

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('fruit-dropdown', 'value')]
)
def update_graph(selected_fruit):
    if selected_fruit is None:
        selected_fruit = []
    elif not isinstance(selected_fruit, list):
        selected_fruit = [selected_fruit]

    filtered_fruits = []
    filtered_prices = []

    for fruit in selected_fruit:
        filtered_fruits.append(fruit)
        fruit_index = data['Fruits'].index(fruit)
        filtered_prices.append(data['Prices'][fruit_index])

    figure = {
        'data': [{
            'x': filtered_fruits,
            'y': filtered_prices,
            'type': 'line+markers',
            'name': 'Fruit Prices'
        }],
        'layout': {
            'title': 'Prices of Selected Fruits',
            'xaxis': {'title': 'Fruits'},
            'yaxis': {'title': 'Prices ($)'}
        }
    }
    return figure


if __name__ == "__main__":
    app.run(debug=True)



