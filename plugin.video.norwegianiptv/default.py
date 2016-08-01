# denmark television plugin written by IPTVxtra
# -*- coding: utf-8 -*-

# for more info please visit http://www.iptvxtra.net

import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)


add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 1'},img='http://static.vg.no/tv-guide/logo/nrktv1.png?1422603334')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 2'},img='http://static.vg.no/tv-guide/logo/nrktv2.png?1422603334')
add_video_item('https://nrk3us-f.akamaihd.net/i/nrk3us_0@107233/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 3'},img='http://static.vg.no/tv-guide/logo/nrk3.png?1422603334')
add_video_item('https://nrksuper-lh.akamaihd.net/i/nrksupertvus_0@108447/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK Super'},img='http://static.vg.no/tv-guide/logo/nrksuper.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS1/.smil/manifest.f4m',{ 'title': 'TV2'},img='https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/TV_2_(Norway)_logo.svg/36px-TV_2_(Norway)_logo.svg.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive08-i.akamaihd.net/hds/live/960206/TVNOHD/master.f4m',{ 'title': 'TV Norge'},img='http://static.vg.no/tv-guide/logo/tvn.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive07-i.akamaihd.net/hds/live/950205/FEMNOHD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'FEM'},img='http://static.vg.no/tv-guide/logo/fem.png?1448888444')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive05-i.akamaihd.net/hds/live/960202/MAXNOHD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'MAX'},img='http://static.vg.no/tv-guide/logo/max.png?1448888447')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive08-i.akamaihd.net/hds/live/950207/VOXNOHD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'VOX'},img='http://static.vg.no/tv-guide/logo/voxno.png?1448888449')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS2/.smil/manifest.f4m',{ 'title': 'TV2 Zebra'},img='http://static.vg.no/tv-guide/logo/tv2zebra.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS3/.smil/manifest.f4m',{ 'title': 'TV2 Nyhetskanalen'},img='http://static.vg.no/tv-guide/logo/tv2nyhet.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS4/.smil/manifest.f4m',{ 'title': 'TV2 Humor'},img='http://static.vg.no/tv-guide/logo/tv2film.png?1427810746')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS8/.smil/manifest.f4m',{ 'title': 'TV2 Livstil'},img='http://static.vg.no/tv-guide/logo/tv2bliss.png?1446469237')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive04-i.akamaihd.net/hds/live/960200/DNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Discovery Channel'},img='http://static.vg.no/tv-guide/logo/discov.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive06-i.akamaihd.net/hds/live/960203/TLCNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'TLC'},img='http://static.vg.no/tv-guide/logo/dtravel.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive06-i.akamaihd.net/hds/live/950780/APNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Animal Planet'},img='http://static.vg.no/tv-guide/logo/animal.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive10-i.akamaihd.net/hds/live/960801/IDNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Investigation Discovery'},img='http://www.polariscable.com/wp-content/uploads/2011/04/investigation-discovery.png')

add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive09-i.akamaihd.net/hds/live/960720/ESNOHD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Eurosport Norge'},img='http://static.vg.no/tv-guide/logo/eurono.png?1455107711')
add_video_item('http://unilivemtveu-lh.akamaihd.net/i/mtvno_1@346424/master.m3u8',{ 'title': 'MTV Norge'},img='http://static.vg.no/tv-guide/logo/mtv.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS7/.smil/manifest.f4m',{ 'title': 'C MORE Action'},img='http://sumo.tv2.no/gfx/channels/920074.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS8/.smil/manifest.f4m',{ 'title': 'C MORE First'},img='http://sumo.tv2.no/gfx/channels/920072.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS9/.smil/manifest.f4m',{ 'title': 'C MORE Hits'},img='http://sumo.tv2.no/gfx/channels/920073.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS10/.smil/manifest.f4m',{ 'title': 'C MORE Emotion'},img='http://sumo.tv2.no/gfx/channels/920075.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS5/.smil/manifest.f4m',{ 'title': 'TV2 Sportskanalen'},img='http://static.vg.no/tv-guide/logo/tv2sport.png?1422603334')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:LS6/.smil/manifest.f4m',{ 'title': 'TV2 Sport Premium'},img='http://sumo.tv2.no/gfx/channels/433127.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS12/.smil/manifest.f4m',{ 'title': 'TV2 Sport Premium 2'},img='http://sumo.tv2.no/gfx/channels/733179.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS13/.smil/manifest.f4m',{ 'title': 'TV2 Sport Premium 3'},img='http://sumo.tv2.no/gfx/channels/733180.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS18/.smil/manifest.f4m',{ 'title': 'TV2 Sport Premium 4'},img='http://sumo.tv2.no/gfx/channels/920065.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS21/.smil/manifest.f4m',{ 'title': 'TV2 Sport Premium 5 / C More Live HD'},img='http://sumo.tv2.no/gfx/channels/920061.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS19/.smil/manifest.f4m',{ 'title': 'C More Tennis'},img='http://sumo.tv2.no/gfx/channels/920058.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive09-i.akamaihd.net/hds/live/950781/DWNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Discovery World'},img='http://tv.tecnotv.net/logo/Discovery%20World.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://dnordichdslive06-i.akamaihd.net/hds/live/960800/SCNOSD/master.f4m&auth=None&proxy=None&simpledownloader=False',{ 'title': 'Discovery Science'},img='https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Science_Channel_logo.svg/112px-Science_Channel_logo.svg.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS22/.smil/manifest.f4m',{ 'title': 'C More Hockey HD'},img='http://sumo.tv2.no/gfx/channels/920058.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS6/.smil/manifest.f4m',{ 'title': 'SF Kanalen'},img='http://sumo.tv2.no/gfx/channels/920076.png')
add_video_item('plugin://plugin.video.f4mTester/?url=http://tv2-hls-live.telenorcdn.net/wzlive/_definst_/amlst:WS32/.smil/manifest.f4m',{ 'title': 'MUTV'},img='http://sumo.tv2.no/gfx/channels/727992.png')
add_video_item('http://static.france24.com/live/F24_EN_LO_HLS/live_ios.m3u8',{ 'title': 'France 24'},img='http://www.france24.com/bundles/aefhermesf24/img/france24-logo.png?version=20160712160254')

xbmcplugin.endOfDirectory(plugin_handle)

