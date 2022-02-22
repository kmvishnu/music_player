import { INITIAL_STATE,AUTH,SEARCH } from "../constants/storeConstants"


export const rootReducer = (state = INITIAL_STATE,action) =>{
  switch(action.type){
    case SEARCH :
      return {...state,keyword:action.payload}

    case AUTH:
      return {...state,isAuth:action.payload}
    
    default:
      return state
  }
}