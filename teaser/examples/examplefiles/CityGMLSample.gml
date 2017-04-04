<?xml version="1.0" ?>
<core:CityModel xmlns:bldg="http://www.opengis.net/citygml/building/2.0" xmlns:core="http://www.opengis.net/citygml/2.0" xmlns:gml="http://www.opengis.net/gml" xmlns:xlink="http://www.w3.org/1999/xlink">
	<gml:name>Simple 3D city model LOD2 without Appearance</gml:name>
	<gml:boundedBy>
		<gml:Envelope srsDimension="3" srsName="urn:ogc:def:crs,crs:EPSG::25832,crs:EPSG::5783">
			<gml:lowerCorner>458868.0 5438343.0 112.0</gml:lowerCorner>
			<gml:upperCorner>458892.0 5438362.0 117.0</gml:upperCorner>
		</gml:Envelope>
	</gml:boundedBy>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Office_lod20</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">24.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>6</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod2Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_ground"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_roof"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_side_north"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_side_south"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_side_east"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod20_side_west"/>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod2Solid>
			<bldg:boundedBy>
				<bldg:GroundSurface gml:id="BSO_Office_lod20_ground">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291473.5 5630136.0 172.0 291473.5 5630181.0 172.0 291613.5 5630181.0 172.0 291613.5 5630136.0 172.0 291473.5 5630136.0 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:GroundSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="BSO_Office_lod20_roof">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291473.5 5630136.0 196.0 291613.5 5630136.0 196.0 291613.5 5630181.0 196.0 291473.5 5630181.0 196.0 291473.5 5630136.0 196.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod20_side_north">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291473.5 5630181.0 172.0 291473.5 5630181.0 196.0 291613.5 5630181.0 196.0 291613.5 5630181.0 172.0 291473.5 5630181.0 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod20_side_south">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291473.5 5630136.0 172.0 291613.5 5630136.0 172.0 291613.5 5630136.0 196.0 291473.5 5630136.0 196.0 291473.5 5630136.0 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod20_side_east">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291613.5 5630136.0 172.0 291613.5 5630181.0 172.0 291613.5 5630181.0 196.0 291613.5 5630136.0 196.0 291613.5 5630136.0 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod20_side_west">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291473.5 5630136.0 172.0 291473.5 5630136.0 196.0 291473.5 5630181.0 196.0 291473.5 5630181.0 172.0 291473.5 5630136.0 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Office_lod21</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">24.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>6</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod2Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_ground"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_roof"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_side_north"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_side_south"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_side_east"/>
							<gml:surfaceMember xlink:href="BSO_Office_lod21_side_west"/>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod2Solid>
			<bldg:boundedBy>
				<bldg:GroundSurface gml:id="BSO_Office_lod21_ground">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630193.5 172.0 291496.0 5630228.5 172.0 291566.0 5630228.5 172.0 291566.0 5630193.5 172.0 291496.0 5630193.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:GroundSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="BSO_Office_lod21_roof">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630193.5 196.0 291566.0 5630193.5 196.0 291566.0 5630228.5 196.0 291496.0 5630228.5 196.0 291496.0 5630193.5 196.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod21_side_north">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630228.5 172.0 291496.0 5630228.5 196.0 291566.0 5630228.5 196.0 291566.0 5630228.5 172.0 291496.0 5630228.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod21_side_south">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630193.5 172.0 291566.0 5630193.5 172.0 291566.0 5630193.5 196.0 291496.0 5630193.5 196.0 291496.0 5630193.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod21_side_east">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291566.0 5630193.5 172.0 291566.0 5630228.5 172.0 291566.0 5630228.5 196.0 291566.0 5630193.5 196.0 291566.0 5630193.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Office_lod21_side_west">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630193.5 172.0 291496.0 5630193.5 196.0 291496.0 5630228.5 196.0 291496.0 5630228.5 172.0 291496.0 5630193.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Office_lod10</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">36.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>9</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod1Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630240.5 172.0 291496.0 5630285.5 172.0 291566.0 5630285.5 172.0 291566.0 5630240.5 172.0 291496.0 5630240.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630240.5 208.0 291566.0 5630240.5 208.0 291566.0 5630285.5 208.0 291496.0 5630285.5 208.0 291496.0 5630240.5 208.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630285.5 172.0 291496.0 5630285.5 208.0 291566.0 5630285.5 208.0 291566.0 5630285.5 172.0 291496.0 5630285.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630240.5 172.0 291566.0 5630240.5 172.0 291566.0 5630240.5 208.0 291496.0 5630240.5 208.0 291496.0 5630240.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291566.0 5630240.5 172.0 291566.0 5630285.5 172.0 291566.0 5630285.5 208.0 291566.0 5630240.5 208.0 291566.0 5630240.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291496.0 5630240.5 172.0 291496.0 5630240.5 208.0 291496.0 5630285.5 208.0 291496.0 5630285.5 172.0 291496.0 5630240.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod1Solid>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Office_lod11</gml:name>
			<bldg:function>1120</bldg:function>
			<bldg:yearOfConstruction>1985</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">32.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>8</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod1Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291581.0 5630202.5 172.0 291581.0 5630272.5 172.0 291616.0 5630272.5 172.0 291616.0 5630202.5 172.0 291581.0 5630202.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291581.0 5630202.5 204.0 291616.0 5630202.5 204.0 291616.0 5630272.5 204.0 291581.0 5630272.5 204.0 291581.0 5630202.5 204.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291581.0 5630272.5 172.0 291581.0 5630272.5 204.0 291616.0 5630272.5 204.0 291616.0 5630272.5 172.0 291581.0 5630272.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291581.0 5630202.5 172.0 291616.0 5630202.5 172.0 291616.0 5630202.5 204.0 291581.0 5630202.5 204.0 291581.0 5630202.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291616.0 5630202.5 172.0 291616.0 5630272.5 172.0 291616.0 5630272.5 204.0 291616.0 5630202.5 204.0 291616.0 5630202.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291581.0 5630202.5 172.0 291581.0 5630202.5 204.0 291581.0 5630272.5 204.0 291581.0 5630272.5 172.0 291581.0 5630202.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod1Solid>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Residential_lod20</gml:name>
			<bldg:function>1000</bldg:function>
			<bldg:yearOfConstruction>1950</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">12.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>2</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod2Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_ground"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_roof1"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_roof2"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_side_north"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_side_south"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_side_east"/>
							<gml:surfaceMember xlink:href="BSO_Residential_lod20_side_west"/>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod2Solid>
			<bldg:boundedBy>
				<bldg:GroundSurface gml:id="BSO_Residential_lod20_ground">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291659.4951905284 5630160.4198729815 172.0 291646.5048094716 5630152.9198729815 172.0 291641.5048094716 5630161.5801270185 172.0 291654.4951905284 5630169.0801270185 172.0 291659.4951905284 5630160.4198729815 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:GroundSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="BSO_Residential_lod20_roof1">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291654.4951905284 5630169.0801270185 179.0 291641.5048094716 5630161.5801270185 179.0 291644.0048094716 5630157.25 184.0 291656.9951905284 5630164.75 184.0 291654.4951905284 5630169.0801270185 179.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:RoofSurface gml:id="BSO_Residential_lod20_roof2">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291659.4951905284 5630160.4198729815 179.0 291656.9951905284 5630164.75 184.0 291644.0048094716 5630157.25 184.0 291646.5048094716 5630152.9198729815 179.0 291659.4951905284 5630160.4198729815 179.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:RoofSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Residential_lod20_side_north">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291646.5048094716 5630152.9198729815 172.0 291646.5048094716 5630152.9198729815 179.0 291644.0048094716 5630157.25 184.0 291641.5048094716 5630161.5801270185 179.0 291641.5048094716 5630161.5801270185 172.0 291646.5048094716 5630152.9198729815 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Residential_lod20_side_south">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291659.4951905284 5630160.4198729815 172.0 291654.4951905284 5630169.0801270185 172.0 291654.4951905284 5630169.0801270185 179.0 291656.9951905284 5630164.75 184.0 291659.4951905284 5630160.4198729815 179.0 291659.4951905284 5630160.4198729815 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Residential_lod20_side_east">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291654.4951905284 5630169.0801270185 172.0 291641.5048094716 5630161.5801270185 172.0 291641.5048094716 5630161.5801270185 179.0 291654.4951905284 5630169.0801270185 179.0 291654.4951905284 5630169.0801270185 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
			<bldg:boundedBy>
				<bldg:WallSurface gml:id="BSO_Residential_lod20_side_west">
					<bldg:lod2MultiSurface>
						<gml:MultiSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291659.4951905284 5630160.4198729815 172.0 291659.4951905284 5630160.4198729815 179.0 291646.5048094716 5630152.9198729815 179.0 291646.5048094716 5630152.9198729815 172.0 291659.4951905284 5630160.4198729815 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:MultiSurface>
					</bldg:lod2MultiSurface>
				</bldg:WallSurface>
			</bldg:boundedBy>
		</bldg:Building>
	</core:cityObjectMember>
	<core:cityObjectMember>
		<bldg:Building>
			<gml:name>BSO_Residential_lod10</gml:name>
			<bldg:function>1000</bldg:function>
			<bldg:yearOfConstruction>1950</bldg:yearOfConstruction>
			<bldg:measuredHeight uom="m">12.0</bldg:measuredHeight>
			<bldg:storeysAboveGround>2</bldg:storeysAboveGround>
			<bldg:storeyHeightsAboveGround uom="m">4.0</bldg:storeyHeightsAboveGround>
			<bldg:lod1Solid>
				<gml:Solid>
					<gml:exterior>
						<gml:CompositeSurface>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291645.5 5630243.5 172.0 291645.5 5630258.5 172.0 291655.5 5630258.5 172.0 291655.5 5630243.5 172.0 291645.5 5630243.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291645.5 5630243.5 184.0 291655.5 5630243.5 184.0 291655.5 5630258.5 184.0 291645.5 5630258.5 184.0 291645.5 5630243.5 184.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291645.5 5630258.5 172.0 291645.5 5630258.5 184.0 291655.5 5630258.5 184.0 291655.5 5630258.5 172.0 291645.5 5630258.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291645.5 5630243.5 172.0 291655.5 5630243.5 172.0 291655.5 5630243.5 184.0 291645.5 5630243.5 184.0 291645.5 5630243.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291655.5 5630243.5 172.0 291655.5 5630258.5 172.0 291655.5 5630258.5 184.0 291655.5 5630243.5 184.0 291655.5 5630243.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
							<gml:surfaceMember>
								<gml:Polygon>
									<gml:exterior>
										<gml:LinearRing>
											<gml:posList>291645.5 5630243.5 172.0 291645.5 5630243.5 184.0 291645.5 5630258.5 184.0 291645.5 5630258.5 172.0 291645.5 5630243.5 172.0</gml:posList>
										</gml:LinearRing>
									</gml:exterior>
								</gml:Polygon>
							</gml:surfaceMember>
						</gml:CompositeSurface>
					</gml:exterior>
				</gml:Solid>
			</bldg:lod1Solid>
		</bldg:Building>
	</core:cityObjectMember>
</core:CityModel>
