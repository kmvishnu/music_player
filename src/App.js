import './App.css';
import Sidebar from './components/Sidebar'
import {  Route, Routes,  } from 'react-router';
import Signin from './components/Signin'
import Signup from './components/Signup'
import Auth from './components/Auth';

function App() {

  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Signin/>}/>
        <Route path="/sidebar" element={<Auth><Sidebar/></Auth>}/>
        <Route path="/signup" element={<Signup/>}/>   
      </Routes>
    </div>
  );
}

export default App;
