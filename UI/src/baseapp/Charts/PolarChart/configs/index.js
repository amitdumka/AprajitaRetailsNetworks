/**
=========================================================
* Aprajita Retails Dashboard - v1.0.1
=========================================================

* Product Page: https://www.aprajitaretails.in/amitkumar/product/soft-ui-dashboard-react
* Copyright 2023 Amit Kumar (https://www.aprajitaretails.in/amitkumar)

Coded by Amit Kumar (www.aprajitaretails.in/amitkumar)

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

/* eslint-disable no-dupe-keys */
// Aprajita Retails Dashboard base styles
import colors from "assets/theme/base/colors";

const { gradients, dark } = colors;

function configs(labels, datasets) {
  const backgroundColors = [];

  if (datasets.backgroundColors) {
    datasets.backgroundColors.forEach((color) =>
      gradients[color]
        ? backgroundColors.push(gradients[color].state)
        : backgroundColors.push(dark.main)
    );
  } else {
    backgroundColors.push(dark.main);
  }

  return {
    data: {
      labels,
      datasets: [
        {
          label: datasets.label,
          backgroundColor: backgroundColors,
          data: datasets.data,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  };
}

export default configs;
