import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import MuiDrawer from '@mui/material/Drawer';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import CssBaseline from '@mui/material/CssBaseline';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Player from './Player'
import FavoriteIcon from '@mui/icons-material/Favorite';
import PlaylistPlayIcon from '@mui/icons-material/PlaylistPlay';
import Table from './Table'
import Search from './Search'
import { useState,useEffect } from 'react';
import axios from 'axios';
import { useDispatch, useSelector } from 'react-redux';
import { ADDPLAY, AUTH, SHOWFAV } from '../store/constants/storeConstants';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import { red } from '@mui/material/colors';
import PowerSettingsNewIcon from '@mui/icons-material/PowerSettingsNew';
import { useNavigate } from 'react-router';
import { CLICKED } from '../store/constants/storeConstants';
import HomeIcon from '@mui/icons-material/Home';
import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import Button from '@mui/material/Button';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';


const drawerWidth = 240;

const openedMixin = (theme) => ({
  width: drawerWidth,
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: 'hidden',
});

const closedMixin = (theme) => ({
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: 'hidden',
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up('sm')]: {
    width: `calc(${theme.spacing(9)} + 1px)`,
  },
});

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
    boxSizing: 'border-box',
    ...(open && {
      ...openedMixin(theme),
      '& .MuiDrawer-paper': openedMixin(theme),
    }),
    ...(!open && {
      ...closedMixin(theme),
      '& .MuiDrawer-paper': closedMixin(theme),
    }),
  }),
);

export default function MiniDrawer() {
  const theme = useTheme();
  const [open, setOpen] = React.useState(false);
  const [songs,setSongs] = useState(0)
  const [loading,setLoading] =useState(true)
  const [currentSong,SetCurrentSong] = useState(4)
  const [keyword,setKeyword] = useState("")
  const UserDetails =useSelector(state=>state.UserDetails)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const showFav =useSelector(state=>state.showFav)
  

  const [visible,setVisible] = useState(false)
  console.log("details",UserDetails)

  const closePlay = (index) => {
    console.log(index)
    UserDetails.playlist.splice(index,1)
    console.log("after removing",UserDetails.playlist)
    dispatch({type:ADDPLAY,payload:UserDetails.playlist})
    let f2 = {"email":UserDetails.email,"playlist":UserDetails['playlist']}
    axios.put("http://127.0.0.1:5001/addPlaylist",f2).then((response)=>{
    }).catch(error=>console.log(error))


  }

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

 
   
  useEffect(()=>{
    axios.get("http://127.0.0.1:5000/findmusic").then(
        (response)=>{
          setSongs(response.data)
          setLoading(false)
        }).catch(
            error=>console.log(error))}
            ,[])

  if (loading){
    return <div className='hi'>Loading</div>
  }
  return (
    <div className='hi'>
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar position="fixed" open={open}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{
              marginRight: '36px',
              ...(open && { display: 'none' }),
            }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            V-MUSIC
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer variant="permanent" open={open}>
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
          </IconButton>
        </DrawerHeader>
        <Divider />
            <List>
              {[["Hi, "+UserDetails.name,<AccountCircleOutlinedIcon />]].map((text, index) => (
                <ListItem key={text[0]}>
                  <ListItemIcon>
                    {text[1]}
                  </ListItemIcon>
                  <ListItemText primary={text[0]} />
                  </ListItem>
              ))}
            </List>
        
        <Divider />
        <List>
          {[['Favourites',(showFav)?<FavoriteIcon style={{ color: red[500]}}/>:<FavoriteBorderIcon/>,()=>dispatch({type:SHOWFAV,payload:!showFav})],['Home', <HomeIcon/>,()=>dispatch({type:CLICKED,payload:''})],['Log Out',<PowerSettingsNewIcon/>,()=>{dispatch({type:AUTH,payload:false}) ; navigate("/")}]].map((text, index) => (
            <ListItem button onClick={text[2]} key={text[0]}>
              <ListItemIcon>
                {text[1]}
              </ListItemIcon>
              <ListItemText primary={text[0]} />
            </ListItem>
          ))}
        </List>
        <Divider />
        
        <List>
          {[['Playlist',<PlaylistPlayIcon />,()=>setVisible(!visible)]].map((text, index) => (
            <ListItem button onClick={text[2]} key={text[0]}>
              <ListItemIcon>
                {text[1]}
              </ListItemIcon>
              <ListItemText primary={text[0]} />
              </ListItem>
          ))}
        </List>
        { visible && (<List>
          <ul>
          {UserDetails['playlist'].map((text, index) => (
            <li>
            <ListItem button onClick={()=>dispatch({type:CLICKED,payload:index})} key={text[0]}>

              <ListItemText primary={text[0]} />
              <Button onClick={()=>closePlay(index)}>
                 <CloseOutlinedIcon/>
              </Button>
              </ListItem>
              </li>
          ))}
          </ul>
        </List>)}
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        <Search keyword={keyword} setKeyword={setKeyword}/>
        <div className='MYstyle'><Player songs={songs} currentSong={currentSong} SetCurrentSong={SetCurrentSong}  /></div>   
        <div> <br/><Table songs={songs} currentSong={currentSong} SetCurrentSong={SetCurrentSong} keyword={keyword}/></div>   
      </Box>
    </Box></div>
  );
}
