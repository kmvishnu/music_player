export const INITIAL_STATE ={
  keyword:"",
  isAuth:false,
  currentUser:{"email":"","password":""},
  UserDetails:{"favourite":[]},
  showFav:false
}

export const AUTH = "AUTH"
export const USER = "USER"
export const ADDFAV ="ADDFAV"
export const USERDETAILS = "USERDETAILS"
export const SHOWFAV ="SHOWFAV"