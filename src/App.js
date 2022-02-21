import logo from './logo.svg';
import './App.css';
import Sidebar from './components/Sidebar'
import NEW from './components/NEW'
import { Route, Routes } from 'react-router';
import Signin from './components/Signin'
import Signup from './components/Signup'
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Signin/>}></Route>
        <Route path="/sidebar" element={<Sidebar/>}/>
        <Route path="/signup" element={<Signup/>}/>
        
      </Routes>
      {/*  <Sidebar/> */}
    </div>
  );
}

export default App;
