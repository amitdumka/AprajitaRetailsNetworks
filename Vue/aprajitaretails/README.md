#Things to Do 

#Team Section 
  There should be a list which will show all location or make it static
 
#Header and title of app need to set once and will be used in all pages using variable or state


# days.js  check for use
# Nuxt Calendly check for use and implement
# Vcandler same as above
# Nuxt Modules check for use and implement
 Link https://nuxt.com/modules

# SupaBase  For Auth 

# Fonts 
 Many Fonts option available , use as desroed as possible
# SnackBar is added
  Check for uses and how to use

 #DataGrid 
 vue3-datagrid
 syncfusion datagrid 


 #Syncfusion datagrid
  need to import 
  "dependencies": { 

    "@syncfusion/ej2-vue-grids": "*", 

    ---

    "vue-class-component": "^8.0.0-rc.1" 

  }, 
  npm i --legacy-peer-deps // use this if npm version is higher than 7
  code below:
  
  import {
  ColumnChooser,
  ColumnDirective,
  ColumnsDirective,
  CommandColumn,
  ContextMenu,
  Edit,
  ExcelExport,
  Filter,
  ForeignKey,
  Freeze,
  Grid,
  GridComponent,
  Group,
  Page,
  PdfExport,
  Reorder,
  Resize,
  RowDD,
  Search,
  Selection,
  Sort,
  Toolbar,
} from '@syncfusion/ej2-vue-grids'

Grid.Inject(CommandColumn)
Grid.Inject(ColumnChooser)
Grid.Inject(ContextMenu)
Grid.Inject(Edit)
Grid.Inject(ExcelExport)
Grid.Inject(Filter)
Grid.Inject(ForeignKey)
Grid.Inject(Freeze)
Grid.Inject(Group)
Grid.Inject(Page)
Grid.Inject(PdfExport)
Grid.Inject(Reorder)
Grid.Inject(Resize)
Grid.Inject(RowDD)
Grid.Inject(Search)
Grid.Inject(Selection)
Grid.Inject(Sort)
Grid.Inject(Toolbar)

export default {
  data() {
    return {}
  },
  components: {
    'ejs-grid': GridComponent,
    'e-columns': ColumnsDirective,
    'e-column': ColumnDirective,
  },
}

Country name and state and city
//Get Auth Token 
var req = unirest("GET", "https://www.universal-tutorial.com/api/getaccesstoken");

  req.headers({
    "Accept": "application/json",
    "api-token": "AuXnFjES43NqbdODZoc1anLtpO9op_9HsA7hqU56HJoxlbbNrMsUAzmsp6cqoZ0HhWQ",
    "user-email": "abc@gmail.com"
  });

{
  "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJtdmdhZGFnaUBnbWFpbC5jb20ifSwiZXhwIjoxNTY2MjM0ODU0fQ.nMWPN38zptwwDKAo11bFyjhCRuzNhZc6NqqCaYJVxP0"
}

var req = unirest("GET", "https://www.universal-tutorial.com/api/countries/");

req.headers({
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVzZXJfZW1haWwiOiJtdmdhZGFnaUBnbWFpbC5jb20ifSwiZXhwIjoxNTY2MjM0ODU0fQ.nMWPN38zptwwDKAo11bFyjhCRuzNhZc6NqqCaYJVxP0",
  "Accept": "application/json"
});

[
  {
    "country_name": "Afghanistan",
    "country_short_name": "AF",
    "country_phone_code": 93
  },
  {
    "country_name": "Albania",
    "country_short_name": "AL",
    "country_phone_code": 355
  },
  {
    "country_name": "Zimbabwe",
    "country_short_name": "ZW",
    "country_phone_code": 263
  }
]

Request : GET https://www.universal-tutorial.com/api/states/United States
[
  {
      "state_name": "Alabama"
  },
  {
      "state_name": "Alaska"
  },
  {
      "state_name": "Arizona"
  },
  {
      "state_name": "Arkansas"
  },
  {
      "state_name": "Byram"
  },
  {
    "state_name": "Wyoming"
  }
]
Request : GET https://www.universal-tutorial.com/api/cities/Alaska
[
  {
      "city_name": "Anchorage"
  },
  {
      "city_name": "Barrow"
  },
  {
      "city_name": "Bethel"
  },
  {
    "city_name": "Wasilla"
  }
]


Cache all this info in local json file , so no need to all always
https://github.com/prograhammer/countries-regions-cities
https://unece.org/trade/uncefact/unlocode
https://www.back4app.com/database/back4app/list-of-all-continents-countries-cities/get-started/javascript/rest-api/fetch
this is awesome data present over net
