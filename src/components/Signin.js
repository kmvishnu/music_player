import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { useNavigate } from 'react-router';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { AUTH, USER } from '../store/constants/storeConstants'
import { useState } from 'react';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import SupervisedUserCircleOutlinedIcon from '@mui/icons-material/SupervisedUserCircleOutlined';
import "./Info.css";


export default function SignInSide() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const [user,setUser] = React.useState({'email':'','password':''})
  const handler = (e) =>{
    setUser({...user,[e.target.id]:e.target.value})
  }
  const Submit = () => {
    axios.post("http://127.0.0.1:5001/loginPage",user).then((response)=>{
      dispatch({type:AUTH,payload:true})
      dispatch({type:USER,payload:user})
      navigate("/sidebar")
      
    }).catch((error)=>document.getElementById("ptag").innerText = "Invalid Credentials")
    
  };
  const [modal, setmodal] = useState(false);
  const [Modal, setModal] = useState(false);

const toggleModal = () => {
  setModal(!Modal);
 
};

const togglemodal = () => {
  setmodal(!modal);
 
};



  return (<>
  
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage: 'url(https://i.pinimg.com/originals/13/8a/bf/138abf84decb70700d30f1eb4a5df042.png)',
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Box component="form" noValidate  sx={{ mt: 1 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
                onChange={(e)=>handler(e)}
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={(e)=>handler(e)}
              />
                 <Grid item xs={12}>
                <p id='ptag' style={{color:"red"}}></p>
              </Grid>
           
              <Button
                type="button"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
                onClick={()=>Submit()}
              >
                Sign In
              </Button>
            
              <Link to="/signup">
                Don't have an account? Sign Up
              </Link>
                       
            </Box>
          </Box>
          <Button onClick={()=>toggleModal()}><InfoOutlinedIcon/></Button>
          <Button onClick={()=>togglemodal()}><SupervisedUserCircleOutlinedIcon/></Button>
        </Grid>
      </Grid>
   
      {Modal && (
        <div className="model">
          <div onClick={toggleModal} className="overley"></div>
          <div className="model-content">
            <h1 style={{fontFamily:"monospace",fontStyle:"italic",color:"aqua"}}>V - Music</h1>
            <p style={{fontFamily:"monospace",fontStyle:"italic"}}>Life is a song... Sing it.</p>
            
                                 
                                
          </div>
        </div>
      )}
      
      {modal && (
        <div className="model">
          <div onClick={togglemodal} className="overley"></div>
          <div className="model-content">
            <h1 style={{fontFamily:"monospace",fontStyle:"italic",color:"aqua"}}>Members</h1>
            <ul>
            <li style={{fontFamily:"monospace",fontStyle:"italic"}}>Vishnu KM</li>
            <li style={{fontFamily:"monospace",fontStyle:"italic"}}>Vishnu B Dev</li>
            <li style={{fontFamily:"monospace",fontStyle:"italic"}}>Vishnu KR</li>
            <li style={{fontFamily:"monospace",fontStyle:"italic"}}>Vishnu Raju</li>            
            </ul>                    
          </div>
        </div>
      )}
      </>
  );
}