from shiny import App, render, ui

# Title of the page

# Import modules for plot rendering
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_slider("number_of_bins", "Number of bins", 1, 100, 20),  # Set a minimum of 1 bin
    ui.output_plot("plot"),
)

def server(input, output, session):   
    @output
    @render.plot(alt="A histogram")
    def plot():
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(437)
        plt.clf()  # Clear the previous plot
        plt.hist(x, bins=input.number_of_bins(), density=True, color= "skyblue")  # Use input.number_of_bins() instead of input.n()
        plt.title("Histogram")
        plt.xlabel("Value")
        plt.ylabel("Density")

app = App(app_ui, server, debug=True)
