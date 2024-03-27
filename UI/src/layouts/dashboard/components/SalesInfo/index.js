import MiniStatisticsCard from "baseapp/Cards/StatisticsCards/MiniStatisticsCard";
import SoftBox from "components/SoftBox";
import Grid from "@mui/material/Grid";

function SalesInfo() {
  return (
    <SoftBox mb={3}>
    <Grid container spacing={3}>
      <Grid item xs={12} sm={6} xl={3}>
        <MiniStatisticsCard
          title={{ text: "today's sale" }}
          count="Rs. 53,000"
          percentage={{ color: "success", text: "+55%" }}
          icon={{ color: "info", component: "paid" }}
        />
      </Grid>
      <Grid item xs={12} sm={6} xl={3}>
        <MiniStatisticsCard
          title={{ text: "monthly sales" }}
          count="2,300"
          percentage={{ color: "success", text: "+3%" }}
          icon={{ color: "info", component: "public" }}
        />
      </Grid>
      <Grid item xs={12} sm={6} xl={3}>
        <MiniStatisticsCard
          title={{ text: "yearly sales" }}
          count="+3,462"
          percentage={{ color: "error", text: "-2%" }}
          icon={{ color: "info", component: "emoji_events" }}
        />
      </Grid>
      <Grid item xs={12} sm={6} xl={3}>
        <MiniStatisticsCard
          title={{ text: "average sales" }}
          count="Rs. 103,430"
          percentage={{ color: "success", text: "+5%" }}
          icon={{
            color: "info",
            component: "shopping_cart",
          }}
        />
      </Grid>
    </Grid>
  </SoftBox>
  );
}

export default SalesInfo