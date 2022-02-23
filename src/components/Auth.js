import { useSelector } from "react-redux"

export default function Auth(props){
  const isAuth = useSelector(state=>state.isAuth)
  if (isAuth === true){
    return props.children
  }
  else{
    console.log("false")
  }
}
