/**
 *  Tables Settings - HRMS
 *  @author - Amit Kumar
 *  @version - 1.0.0
 *  @description - HRMS Tables
 *  @since - 29/03/2024
 */

const employee_table = {
  columns: [
    {
      name: "EmployeeId",
      label: "Employee Id",
      width:100,
      options: {
        filter: true,
        sort: true,
      },
    },
    {
      name: "FirstName",
      label: "First Name",
      width: 100,
      options: {
        filter: true,
        sort: true,
      },
    },
  ],
};

const attendandes_table = {
  columns: [
    {
      name: "EmployeeId",
      label: "Employee Id",
      width:100,
      type: "pk",
      visible:false,
      requried:true,
      options: {
        filter: true,
        sort: true,
      },
    },
    {
      name: "FirstName",
      label: "First Name",
      visible:true,
      width: 100,
      requried:true,
      options: {
        filter: true,
        sort: true,
      },
    },
  ],
};

export { employee_table, attendandes_table };