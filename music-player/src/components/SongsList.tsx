import { List, Button } from 'antd';
import * as React from 'react';
import { connect } from 'react-redux';

import { songsNamesList } from '../data';
import { State } from '../types';


const SongsList = ({ songsToDisplay, currentSongIndex }: { songsToDisplay: string[]; currentSongIndex: number }) => {
  const songToComponent = (song: string, index: number) => (
    <List.Item className="song-item">
      <div className="song">
        {currentSongIndex === index ? <strong>{song}</strong> : song}

        <div className="song-buttons">
          <Button className="add-song-button song-button" shape="circle" icon="plus" size="small"/>
          <Button className="remove-song-button song-button" shape="circle" icon="minus" size="small"/>
        </div>
      </div>

    </List.Item>
  );
  return (
    <div className="songsList">
      <List
        dataSource={songsToDisplay}
        renderItem={songToComponent}
        bordered={true}
      />
    </div>
  );
};

const SongsListConnected = connect((state: State) => ({
  songsToDisplay: getSongsByPlaylist(state.songsListState.currentPlaylistName, state.songsListState.playlists),
  currentSongIndex: state.songsListState.currentSongIndex,
}))(SongsList);
export { SongsListConnected as SongsList };


const getSongsByPlaylist = (playlist: string, playlists: {}): string[] =>
  playlists[playlist].map((index: number) => songsNamesList[index]);