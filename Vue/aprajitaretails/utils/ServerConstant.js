export class ServerContant {
  static get BASE_URL() {
    return 'http://localhost:8000'
  }

  static get API_URL() {
    return `${ServerContant.BASE_URL}/api/`
  }

  static get LOGIN_URL() {
    return `${ServerContant.BASE_URL}/login/`
  }


  static Client='clients'
  static Group='groups'
  static Store='stores'
  static Employee='employees'

  static App_Name='Aprajita Retails'
  static App_Icon='Icon Url or path'


}
