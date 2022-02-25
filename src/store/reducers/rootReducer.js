import { INITIAL_STATE,AUTH,USER,USERDETAILS,ADDFAV,SHOWFAV,ADDPLAY,CLICKED } from "../constants/storeConstants"

export const rootReducer = (state = INITIAL_STATE,action) =>{
  switch(action.type){
    case AUTH:
      return {...state,isAuth:action.payload}

    case USER:
      return {...state,currentUser:action.payload}

    case USERDETAILS:
      return {...state,UserDetails:action.payload}
    
    case ADDFAV:
      return {...state,UserDetails:{...state.UserDetails,favourite:action.payload}}

    case SHOWFAV:
      return {...state,showFav:action.payload}

    case ADDPLAY:
      return {...state,UserDetails:{...state.UserDetails,playlist:action.payload}}

    case CLICKED:
      return {...state,clickedPlay:action.payload}


    default:
      return state
  }
}