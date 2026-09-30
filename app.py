import gradio as gr

from bearing_and_distance_calculator import calculate_results


def calculate(lat1, lon1, lat2, lon2, unit):
    try:
        return calculate_results(lat1, lon1, lat2, lon2, unit)
    except ValueError as exc:
        return str(exc), "", ""
    except Exception as exc:
        return f"Unexpected error: {exc}", "", ""


with gr.Blocks(title="Bearing and Distance Calculator") as demo:
    gr.Markdown("# Bearing and Distance Calculator")
    gr.Markdown(
        "Enter two coordinates in decimal degrees. The tool calculates great-circle distance "
        "using the Haversine formula and initial bearing using the standard spherical bearing formula."
    )

    with gr.Row():
        with gr.Column():
            lat1 = gr.Number(label="Point 1 Latitude", value=None)
            lon1 = gr.Number(label="Point 1 Longitude", value=None)
            lat2 = gr.Number(label="Point 2 Latitude", value=None)
            lon2 = gr.Number(label="Point 2 Longitude", value=None)

            unit = gr.Dropdown(
                label="Distance Units",
                choices=["Kilometers", "Miles", "Nautical Miles"],
                value="Kilometers",
            )

            calculate_btn = gr.Button("Calculate", variant="primary")

        with gr.Column():
            distance_output = gr.Textbox(label="Distance", interactive=False)
            bearing_output = gr.Textbox(label="Initial Bearing", interactive=False)
            back_bearing_output = gr.Textbox(label="Back Bearing", interactive=False)

    gr.Markdown(
        "**Validation:** Latitude must be between -90 and 90. Longitude must be between -180 and 180."
    )

    gr.Markdown(
        "**Disclaimer:** Results are approximate and assume a spherical Earth. For high-precision "
        "geodesy, use ellipsoidal formulas such as Vincenty or Karney."
    )

    calculate_btn.click(
        fn=calculate,
        inputs=[lat1, lon1, lat2, lon2, unit],
        outputs=[distance_output, bearing_output, back_bearing_output],
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
