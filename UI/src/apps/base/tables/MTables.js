import { DataGrid } from "@mui/x-data-grid";
// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";
function MTables(props) {
  const { entities, columns } = props.tableData;

  return (
    <div style={{ height: 300, width: "100%" }}>
      <DataGrid rows={entities} columns={columns} />
    </div>
  );
}

export default MTables;
