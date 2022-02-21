import INITIAL_STATE from './store/storeConstants.js'
export const rootReducer = (state = INITIAL_STATE) =>{
  switch(action.type){
    case SEARCH :
      const newState = {...state,keyword:action.payload}
      return newState
      
    default:
      return state
  }
}