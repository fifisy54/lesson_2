import pandas as pd
import hiplot as hip

pd.pandas.set_option('display.max_columns', None)
pd.set_option("expand_frame_repr", False)
pd.options.display.expand_frame_repr = False


if __name__ == "__main__":
    # загружаем результаты анализа
    hyperparams = pd.read_csv('results.csv')

    temp = hyperparams.columns.tolist()
    cols = temp[-2:] + temp[:-2]
    cols = [cols[1]] + [cols[0]] + cols[2:]
    hyperparams = hyperparams[cols]

    print(hyperparams)

    hyp_hiplot = hip.Experiment.from_dataframe(hyperparams)
    #
    # # Provide configuration for the parallel plot
    # hyp_hiplot.display_data(hip.Displays.PARALLEL_PLOT).update({
    #     # Hide some columns in the parallel plot
    #     'hide': ['uid', 'from_uid'],
    # })
    _ = hyp_hiplot.to_html("plot_selection.html")
