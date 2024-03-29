import { DataGrid } from "@mui/x-data-grid";
// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";
function MTables(props) {
  const { dataSource } = props;

  return (
    <div style={{ height: 300, width: "100%" }}>
      <DataGrid rows={dataSource} />
    </div>
  );
}

export default MTables;
