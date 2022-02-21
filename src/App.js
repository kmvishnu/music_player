import logo from './logo.svg';
import './App.css';
import Sidebar from './components/Sidebar'
import NEW from './components/NEW'
import {  Navigate, Route, Routes, useNavigate } from 'react-router';
import Signin from './components/Signin'
import Signup from './components/Signup'
import { useState } from 'react';

function App() {

  // const[isAuth,setisAuth] = useState(false)
  // const navigate = useNavigate()

  // {<Signin setisAuth={setisAuth}/>}
  
    // const Verify=()=>{
    //   if (isAuth){return <Route path="/sidebar" element={<Sidebar/>}/>}
    //   else {return <Navigate to="/"/>}
    // }
   
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Signin/>}/>
        <Route path="/sidebar" element={<Sidebar/>}/>
        <Route path="/signup" element={<Signup/>}/>
        
      </Routes>
    
    </div>
  );
}

export default App;
