import * as React from 'react';
import {connect} from 'react-redux';

import './App.css';
import {MusicController} from './components/MusicController';
import {PlaylistMenu} from './components/PlaylistMenu';
import {SongsList} from './components/SongsList';
import {State} from './types';
import {getCurrentPlaylist, getCurrentSongIndex} from './selectors';


const App = ({currentSongIndex, currentPlaylist}: {currentSongIndex: number; currentPlaylist: string}) => {
    return (
        <div className="musicPlayer">
            <header className="header">
                <h1>Music Player</h1>
                <h3>Playlist: {currentPlaylist}</h3>
                <MusicController/>
            </header>
            <div className="main">
                <PlaylistMenu/>
                <SongsList/>
            </div>
        </div>
    );
};


const AppConnected = connect((state: State) => ({
    currentSongIndex: getCurrentSongIndex(state),
    currentPlaylist: getCurrentPlaylist(state)
}))(App);
export default AppConnected;
