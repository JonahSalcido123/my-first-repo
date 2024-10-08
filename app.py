{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JonahSalcido123/JonahSalcido123/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "# Title of the app\n",
        "st.title('Interactive Sales Data Visualization App')\n",
        "\n",
        "# Pre-loaded dataset for sales information\n",
        "data = {\n",
        "    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],\n",
        "    'Sales (Thousands USD)': [150, 200, 300, 400, 250],\n",
        "    'Quantity Sold': [30, 45, 55, 65, 50]\n",
        "}\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Display the dataset\n",
        "st.write(\"Sales Data:\")\n",
        "st.write(df)\n",
        "\n",
        "# Let the user select columns for the chart\n",
        "columns = df.columns.tolist()\n",
        "\n",
        "# Dropdowns for X and Y axes selection\n",
        "x_axis = st.selectbox('Select column for X-axis', columns)\n",
        "y_axis = st.selectbox('Select column for Y-axis', columns)\n",
        "\n",
        "# Choose chart type: Bar Chart or Line Chart\n",
        "chart_type = st.selectbox('Select chart type', ['Bar Chart', 'Line Chart'])\n",
        "\n",
        "# Display chart based on user selections\n",
        "if chart_type == 'Bar Chart':\n",
        "    st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))\n",
        "elif chart_type == 'Line Chart':\n",
        "    st.line_chart(df[[x_axis, y_axis]].set_index(x_axis))"
      ],
      "metadata": {
        "id": "S_ZOOsJ73oUX",
        "outputId": "712ccd5b-b696-4745-9c9b-f95a78e40a78",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-10-08 20:42:34.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.755 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.788 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.794 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.814 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.822 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.823 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.832 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.840 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.842 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.843 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.850 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.851 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.858 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.866 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.868 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.876 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.877 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.878 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.884 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:34.886 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:35.189 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-10-08 20:42:35.205 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}