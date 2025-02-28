import marimo

__generated_with = "0.11.12"
app = marimo.App(width="full", theme="dark")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.graph_objects as go
    return go, mo, pd


@app.cell
def _(go, mo, pd):
    def render_home_page():
        return mo.md("# Home Page")

    def render_dulles_page():
        return mo.vstack([
            mo.md("# Dulles Page"),
            mo.md("Trying out the routing capability of marimo")
        ])

    def render_scion_page():
        return mo.vstack([
            mo.md("# Scion Page"),
            mo.md("Hope this works properly")
        ])

    def render_gr86_page():
        return mo.vstack([
            mo.md("# GR86 Dashboard Page"),
            mo.md("If it does work out then Marimo is pretty simple to use")
        ])

    def render_cx9_page():
        return mo.vstack([
            mo.md("# CX9 Dashboard Page"),
            mo.md("The CX9 dashboard is a placeholder for now")
        ])

    def render_cx3_page():
        return mo.vstack([
            mo.md("# CX3 Dashboard Page"),
            mo.md("The CX3 dashboard is not fleshed out yet, coming soon...")
        ])

    def render_bwi_page():

        def test_expensive_component(temp_fig):
            return temp_fig

        df = pd.DataFrame({
            'PROCESSING_DATE': ['2025-02-26', '2025-02-25', '2025-02-24', '2025-02-23', '2025-02-22', '2025-02-21', '2025-02-20'],
            'School': ['MSJ', 'Calvert Hall', 'Howard', 'Longreach', 'Gilman', 'River Hill', 'Loyola Blakefield'],
            'Student Count': [100000, 100, 2020, 109, 2945, 30393, 39281]
        })


        fig = go.Figure(
            go.Scatter(
                x = df['PROCESSING_DATE'],
                y = df['Student Count'],
                mode='lines+markers'
            )
        )
        fig.update_layout(
            autosize=True,
            template="plotly_dark",
            paper_bgcolor="#1d1d1d",
            plot_bgcolor="#1d1d1d",
            font_color="#d7d7d7",
            margin=dict(l=20, r=20, t=30, b=20)
        )
        temp_fig = go.Figure(
            go.Scatter(
                x = df['PROCESSING_DATE'],
                y = df['Student Count'],
                mode='lines+markers'
            )
        )
        temp_fig.update_layout(
            autosize=True,
            template="plotly_dark",
            paper_bgcolor="#1d1d1d",
            plot_bgcolor="#1d1d1d",
            font_color="#d7d7d7",
            margin=dict(l=20, r=20, t=30, b=20)
        )
        fig2 = go.Figure(
            go.Scatter(
                x = df['PROCESSING_DATE'],
                y = df['Student Count'],
                mode='lines+markers'
            )
        )
        fig2.update_layout(
            autosize=True,
            template="plotly_dark",
            paper_bgcolor="#1d1d1d",
            plot_bgcolor="#1d1d1d",
            font_color="#d7d7d7",
            margin=dict(l=20, r=20, t=30, b=20)
        )
        fig3 = go.Figure(
            go.Bar(
                x = df['PROCESSING_DATE'],
                y = df['Student Count']
            )
        )
        fig3.update_layout(
            autosize=True,
            template="plotly_dark",
            paper_bgcolor="#1d1d1d",
            plot_bgcolor="#1d1d1d",
            font_color="#d7d7d7",
            margin=dict(l=20, r=20, t=30, b=20)
        )

        return mo.vstack(
            [
                mo.md("""<h1 style='text-align: center; color: #d7d7d7; padding-bottom: 50px;'>BWI Dashboard Attempt 1</h1>"""),
                mo.hstack(
                    [
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(
                                    test_expensive_component(fig),
                                    config = {
                                        'responsive': True
                                    }
                                ),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        ),
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(temp_fig),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        ),
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(fig2),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        )
                    ],
                    widths='equal',
                    gap = 2
                ),
                mo.hstack(
                    [
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(fig),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        ),
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(temp_fig),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        )
                    ],
                    widths='equal',
                    gap = 2
                ),
                mo.hstack(
                    [
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(fig),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        )
                    ],
                    widths='equal',
                    gap = 2
                ),
                mo.hstack(
                    [
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(fig3),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        ),
                        mo.vstack(
                            [
                                mo.md("## Visualization 2").style({
                                    'margin-top': '0',
                                    'padding-bottom': '0.5rem',
                                    'border-bottom': '1px solid #333',
                                    'color': '#d7d7d7',
                                    'text-align': 'center'
                                }),
                                mo.ui.plotly(test_expensive_component(fig3),
                                    config = {
                                        'responsive': True
                                    }),
                                mo.md("Visualization description example is being written here. This is the same description as the previous visualization. Hopefully this description will wrap. I am writing a long description with the hope that this will exceed the boundary range to test the ability to wrap text and not cut it off.").style({
                                    'text-align': 'center',
                                    'word-break': 'break-word',
                                    'font-style': 'italic',
                                    'color': 'gray',
                                    'font-size': '0.8rem',
                                    'margin-bottom': '5px'
                                })
                            ]
                        )
                    ],
                    widths='equal',
                    gap = 2
                )
            ]
        )
    return (
        render_bwi_page,
        render_cx3_page,
        render_cx9_page,
        render_dulles_page,
        render_gr86_page,
        render_home_page,
        render_scion_page,
    )


@app.cell
def _(
    mo,
    render_bwi_page,
    render_cx3_page,
    render_cx9_page,
    render_dulles_page,
    render_gr86_page,
    render_home_page,
    render_scion_page,
):
    mo.routes({
        "#/": render_home_page,
        "#/airport/bwi": render_bwi_page,
        "#/airport/dulles": render_dulles_page,
        "#/car/toyota/scion": render_scion_page,
        "#/car/toyota/gr86": render_gr86_page,
        "#/car/mazda/cx9": render_cx9_page,
        "#/car/mazda/cx3": render_cx3_page,
        mo.routes.DEFAULT: render_home_page
    })
    return


@app.cell
def _(mo):
    mo.sidebar(
        [
            mo.md('# Dashboard Menu'),
            mo.nav_menu(
                {
                    '#/': 'Home',
                    'Airport Dashboards': {
                        '#/airport/bwi': {
                            "label": "BWI Dashboard",
                            "description": "Metrics for flights at BWI airport"
                        },
                        '#/airport/dulles': {
                            "label": "Dulles Dashboard",
                            "description": "Metrics for flights at Dulles airport"
                        }
                    },
                    'Toyota Dashboards': {
                        "#/car/toyota/scion":{
                            "label": "Scion Dashboard",
                            "description": "Metrics on sales for toyota scion cars"
                        },
                        "#/car/toyota/gr86": {
                            "label": "GR86 Dashboard",
                            "description": "Metrics on sales for toyota GR86 cars"
                        }
                    },
                    "Mazda Dashboards": {
                        "#/car/mazda/cx9":{
                            "label": "CX9 Dashboard",
                            "description": "Metrics on sales for mazda CX9 cars"
                        },
                        "#/car/mazda/cx3": {
                            "label": "CX3 Dashboard",
                            "description": "Metrics on sales for toyota CX3 cars"
                        }
                    }
                },
                orientation='vertical'
            )
        ]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
