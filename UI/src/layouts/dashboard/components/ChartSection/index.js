import ReportsBarChart from "baseapp/Charts/BarCharts/ReportsBarChart";
import GradientLineChart from "baseapp/Charts/LineCharts/GradientLineChart";
import reportsBarChartData from "layouts/dashboard/data/reportsBarChartData";
import gradientLineChartData from "layouts/dashboard/data/gradientLineChartData";
// Aprajita Retails React base styles
import typography from "assets/theme/base/typography";

// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Aprajita Retails React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

function ChartSection() {
  const { size } = typography;
  const { chart, items } = reportsBarChartData;
  return (
    <SoftBox mb={3}>
      <Grid container spacing={3}>
        <Grid item xs={12} lg={5}>
          <ReportsBarChart
            title="active users"
            description={
              <>
                (<strong>+23%</strong>) than last week
              </>
            }
            chart={chart}
            items={items}
          />
        </Grid>
        <Grid item xs={12} lg={7}>
          <GradientLineChart
            title="Sales Overview"
            description={
              <SoftBox display="flex" alignItems="center">
                <SoftBox fontSize={size.lg} color="success" mb={0.3} mr={0.5} lineHeight={0}>
                  <Icon className="font-bold">arrow_upward</Icon>
                </SoftBox>
                <SoftTypography variant="button" color="text" fontWeight="medium">
                  4% more{" "}
                  <SoftTypography variant="button" color="text" fontWeight="regular">
                    in 2021
                  </SoftTypography>
                </SoftTypography>
              </SoftBox>
            }
            height="20.25rem"
            chart={gradientLineChartData}
          />
        </Grid>
      </Grid>
    </SoftBox>
  );
}

export default ChartSection;
