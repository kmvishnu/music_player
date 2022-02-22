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
import { AUTH } from '../store/constants/storeConstants'


export default function SignInSide() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const [user,setUser] = React.useState({'email':'','password':''})
  const handler = (e) =>{
    setUser({...user,[e.target.id]:e.target.value})
  }
  const Submit = () => {
    axios.post("http://127.0.0.1:5001/loginPage",user).then((response)=>{
      console.log("USER Found")
      dispatch({type:AUTH,payload:true})
      navigate("/sidebar")
      
    }).catch((error)=>console.log("ERROR is ",error))
    
  };

  return (<>
    {console.log(user)}
      <Grid container component="main" sx={{ height: '100vh' }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage: 'url(https://source.unsplash.com/random)',
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
        </Grid>
      </Grid>
      </>
  );
}