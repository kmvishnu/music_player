import * as React from 'react';
import { styled, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Slider from '@mui/material/Slider';
import IconButton from '@mui/material/IconButton';
import Stack from '@mui/material/Stack';
import PauseRounded from '@mui/icons-material/PauseRounded';
import PlayArrowRounded from '@mui/icons-material/PlayArrowRounded';
import FastForwardRounded from '@mui/icons-material/FastForwardRounded';
import FastRewindRounded from '@mui/icons-material/FastRewindRounded';
import VolumeUpRounded from '@mui/icons-material/VolumeUpRounded';
import VolumeDownRounded from '@mui/icons-material/VolumeDownRounded';
import { useEffect,useState } from 'react';

const Widget = styled('div')(({ theme }) => ({
  padding: 16,
  borderRadius: 16,
  width: '100%',
  maxWidth: '100%',
  margin: 'auto',
  position: 'relative',
  zIndex: 1,
  backgroundColor:
    theme.palette.mode === 'dark' ? 'rgba(0,0,0,0.6)' : 'rgba(255,255,255,0.4)',
  backdropFilter: 'blur(40px)',
}));

const CoverImage = styled('div')({
  width: 100,
  height: 100,
  objectFit: 'cover',
  overflow: 'hidden',
  flexShrink: 0,
  borderRadius: 8,
  backgroundColor: 'rgba(0,0,0,0.08)',
  '& > img': {
    width: '100%',
  },
});

const TinyText = styled(Typography)({
  fontSize: '0.75rem',
  opacity: 0.38,
  fontWeight: 500,
  letterSpacing: 0.2,
});

export default function MusicPlayerSlider(props) {
  // PROPS
  const songs = props.songs
  const currentSong =props.currentSong
  const SetCurrentSong=props.SetCurrentSong
 
//  =================================================================================
  const theme = useTheme();
  // const [duration,setDuration] = useState(0)
  // const [position, setPosition] = React.useState(32);



  const sound = songs[currentSong].url
  const [audio,setAudio] = useState(new Audio(sound));
  const [playing, setPlaying] = useState(false);
  const [change,setChange] = useState(true)
  const [volume,setVolume] = useState(0.5)
  const [cTime,setcTime] =useState(0)
  const changecTime =(e)=>{
    audio.currentTime = e
    setcTime(e)
  }

  useEffect(()=>{  
    if (change)
    {
      audio.play()
      setPlaying(!playing)
      setChange(!change) 
    }
  },[change])
  
  const toggle = () => setPlaying(!playing);
  useEffect(() => {
      playing ? audio.play() : audio.pause();
    },
    [playing]
  );
 
  
  useEffect(()=>{
    audio.pause()
    setPlaying(false)
    setAudio(new Audio(sound))
    setcTime(0)
    setChange(!change)
  },[currentSong])
  
  
  const nextSong =()=>{
    SetCurrentSong(currentSong+1)
  }

  const lastSong =()=>{
    SetCurrentSong(currentSong-1)
  }
//  =================================================================================
  function formatDuration(value) {
    const minute = Math.floor(value / 60);
    let secondLeft = value - minute * 60;
    secondLeft =Math.round(secondLeft)
    return `${minute}:${secondLeft < 9 ? `0${secondLeft}` : secondLeft}`;
  }
  const mainIconColor = theme.palette.mode === 'dark' ? '#fff' : '#000';
  const lightIconColor =
    theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.4)';
  audio.volume = volume

  console.log("current time ",audio.currentTime)
  console.log("current duration ",audio.duration)

  return (
   
    <div >
      
   
    <Box sx={{ width: '100%', overflow: 'hidden' }} >
      <Widget>
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          <CoverImage>
          <img
              src={songs[currentSong].links.images[0].url}
              alt={songs[currentSong].author}
            />
          </CoverImage>
          <Box sx={{ ml: 1.5, minWidth: 0 }}>
            <Typography variant="caption" color="text.secondary" fontWeight={500}>
           Now Playing
            </Typography>
            <Typography noWrap>
              <b>  {songs[currentSong].author}</b>
            </Typography>
            <Typography noWrap letterSpacing={-0.25}>
              {songs[currentSong].name}
            </Typography>
          </Box>
        </Box>
         <Slider
          aria-label="time-indicator"
          size="small"
          value={audio.currentTime}
          min={0}
          step={1}
          max={audio.duration}
          onChange={(e) =>changecTime(e.target.value)}
          sx={{
            color: theme.palette.mode === 'dark' ? '#fff' : 'rgba(0,0,0,0.87)',
            height: 4,
            '& .MuiSlider-thumb': {
              width: 8,
              height: 8,
              transition: '0.3s cubic-bezier(.47,1.64,.41,.8)',
              '&:before': {
                boxShadow: '0 2px 12px 0 rgba(0,0,0,0.4)',
              },
              '&:hover, &.Mui-focusVisible': {
                boxShadow: `0px 0px 0px 8px ${
                  theme.palette.mode === 'dark'
                    ? 'rgb(255 255 255 / 16%)'
                    : 'rgb(0 0 0 / 16%)'
                }`,
              },
              '&.Mui-active': {
                width: 20,
                height: 20,
              },
            },
            '& .MuiSlider-rail': {
              opacity: 0.28,
            },
          }}
        />
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            mt: -2,
          }}
        >
          <TinyText>{formatDuration(audio.currentTime)}</TinyText>
          {/* <TinyText>{formatDuration(audio.duration )}</TinyText> */}
        </Box>
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            mt: -1,
          }}
        >
          <IconButton aria-label="previous song" onClick={()=>lastSong()}>
            <FastRewindRounded fontSize="large" htmlColor={mainIconColor} />
          </IconButton>
          <IconButton
            aria-label={playing ? 'play' : 'pause'}
            onClick={() => toggle() }
          >
            {!playing ? (
              <PlayArrowRounded
                sx={{ fontSize: '3rem' }}
                htmlColor={mainIconColor}
              />
            ) : (
              <PauseRounded sx={{ fontSize: '3rem' }} htmlColor={mainIconColor} />
            )}
          </IconButton>
          <IconButton aria-label="next song" onClick={()=>nextSong()}>
            <FastForwardRounded fontSize="large" htmlColor={mainIconColor} />
          </IconButton>
        </Box>
        <Stack spacing={2} direction="row" sx={{ mb: 1, px: 1 }} alignItems="center">
          <VolumeDownRounded htmlColor={lightIconColor} />
          <Slider
            aria-label="Volume"
            
            
            value={volume}
            min={0}
            step={0.01}
            max={1}
            onChange={(e) => setVolume(e.target.value)}

            sx={{
              color: theme.palette.mode === 'dark' ? '#fff' : 'rgba(0,0,0,0.87)',
              '& .MuiSlider-track': {
                border: 'none',
              },
              '& .MuiSlider-thumb': {
                width: 24,
                height: 24,
                backgroundColor: '#fff',
                '&:before': {
                  boxShadow: '0 4px 8px rgba(0,0,0,0.4)',
                },
                '&:hover, &.Mui-focusVisible, &.Mui-active': {
                  boxShadow: 'none',
                },
              },
            }}
          />
          <VolumeUpRounded htmlColor={lightIconColor} />
        </Stack>
      </Widget>
    </Box>
    </div>
  );
}
