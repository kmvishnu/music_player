import { Navigate } from "react-router"
export default function Auth(props){
  if (props.isAuth === true){
    props.setisAuth(true)
  }
  else{
    return <Navigate to="/"/>
  }
}