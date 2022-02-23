export const INITIAL_STATE ={
  keyword:"",
  isAuth:false,
  currentUser:{"email":"","password":""},
  UserDetails:{"favourite":[],"playlist":[]},
  showFav:false,
  clickedPlay:''
}

export const AUTH = "AUTH"
export const USER = "USER"
export const ADDFAV ="ADDFAV"
export const ADDPLAY = "ADDPLAY"
export const USERDETAILS = "USERDETAILS"
export const SHOWFAV ="SHOWFAV"
export const CLICKED = "CLICKED"