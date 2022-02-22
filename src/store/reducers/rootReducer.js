import { INITIAL_STATE,AUTH,USER } from "../constants/storeConstants"

export const rootReducer = (state = INITIAL_STATE,action) =>{
  switch(action.type){
    case AUTH:
      return {...state,isAuth:action.payload}

    case USER:
      return {...state,currentUser:action.payload}
    
    default:
      return state
  }
}