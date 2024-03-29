
/**
 * SF Table Helper 
 *  It keep all helper functions or methods related to SF Table
 *  to make SFTable more readable and clearner
 */

// Toolbar Options [Default]
const toolbarOptions = [
    "Add",
    "Edit",
    "Delete",
    "Update",
    "Cancel",
    "Print",
    "Search",
    "ColumnChooser",
    "ExcelExport",
    "PdfExport",
  ];
  //Edit Settings
  const editSettings = { allowEditing: true, allowAdding: true, allowDeleting: true };
  //Drop Down Options
  const ddlData = [
    { text: "5 Rows", value: "5" },
    { text: "10 Rows", value: "10" },
    { text: "100 Rows", value: "100" },
    { text: "500 Rows", value: "500" },
  ];
  // Empty row template
  function emptyMessageTemplate() {
    return (
      <div className="emptyRecordTemplate">
        <img
          src="src/grid/images/emptyRecordTemplate.svg"
          className="e-emptyRecord"
          alt="No record"
        />
        <span>No record available.</span>
      </div>
    );
  }

  function toolbarClick(args,gridInstance) {
    switch (args.item.id) {
      case "DefaultExport_pdfexport":
        gridInstance.pdfExport();
        break;
      case "DefaultExport_excelexport":
        gridInstance.excelExport();
        break;
      case "DefaultExport_csvexport":
        gridInstance.csvExport();
        break;
    }
  }
  
  export { toolbarOptions, editSettings, ddlData, emptyMessageTemplate, toolbarClick };